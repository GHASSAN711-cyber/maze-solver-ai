import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER, TA_RIGHT

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# ===============================
# Arabic Font
# ===============================

FONT_PATH = r"C:\Windows\Fonts\arial.ttf"


pdfmetrics.registerFont(
    TTFont(
        "ArialArabic",
        FONT_PATH
    )
)


# ===============================
# PDF Generator
# ===============================


def generate_report(results, analysis):

    folder = "documentation"

    if not os.path.exists(folder):
        os.makedirs(folder)


    file_path = os.path.join(
        folder,
        "final_report.pdf"
    )


    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4
    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "title",
        parent=styles["Title"],
        fontName="ArialArabic",
        alignment=TA_CENTER,
        fontSize=22
    )


    heading_style = ParagraphStyle(
        "heading",
        parent=styles["Heading2"],
        fontName="ArialArabic",
        alignment=TA_RIGHT,
        fontSize=16
    )


    normal_style = ParagraphStyle(
        "normal",
        parent=styles["Normal"],
        fontName="ArialArabic",
        alignment=TA_RIGHT,
        fontSize=12,
        leading=18
    )


    content = []


    # ===============================
    # الغلاف
    # ===============================

    content.append(
        Paragraph(
            "Maze Solver AI",
            title_style
        )
    )


    content.append(
        Spacer(1,40)
    )


    content.append(
        Paragraph(
            "نظام ذكي لحل المتاهات ومقارنة خوارزميات البحث",
            heading_style
        )
    )


    content.append(
        Spacer(1,80)
    )


    content.append(
        Paragraph(
            """
            إعداد الطالب:<br/>
            م. غسان الضريبي
            """,
            normal_style
        )
    )


    content.append(
        Spacer(1,30)
    )


    content.append(
        Paragraph(
            """
            التخصص:<br/>
            هندسة كهربائية
            <br/><br/>
            العام الأكاديمي: 2026
            """,
            normal_style
        )
    )


    content.append(PageBreak())



    # ===============================
    # مقدمة
    # ===============================

    content.append(
        Paragraph(
            "مقدمة المشروع",
            heading_style
        )
    )


    intro = """
    يهدف مشروع Maze Solver AI إلى تصميم نظام ذكي
    يقوم بحل المتاهات باستخدام مجموعة من خوارزميات
    البحث في الذكاء الاصطناعي، مع تحليل ومقارنة
    الأداء حسب سرعة التنفيذ، طول المسار، عدد العقد
    التي تمت زيارتها، واستهلاك الذاكرة.
    """


    content.append(
        Paragraph(
            intro,
            normal_style
        )
    )


    content.append(
        Spacer(1,30)
    )


    # ===============================
    # جدول النتائج
    # ===============================


    content.append(
        Paragraph(
            "نتائج مقارنة الخوارزميات",
            heading_style
        )
    )


    table_data = [

        [
            "الخوارزمية",
            "العقد المزارة",
            "طول المسار",
            "الزمن",
            "الذاكرة"
        ]

    ]


    for r in results:

        table_data.append(

            [

                r["algorithm"],
                str(r["visited"]),
                str(r["path"]),
                str(r["time"]),
                str(r["memory"])+" MB"

            ]

        )


    table = Table(
        table_data
    )


    table.setStyle(

        TableStyle(

            [

                (
                "GRID",
                (0,0),
                (-1,-1),
                0.5,
                None
                ),


                (
                "ALIGN",
                (0,0),
                (-1,-1),
                "CENTER"
                ),


                (
                "FONT",
                (0,0),
                (-1,-1),
                "ArialArabic"
                )

            ]

        )

    )


    content.append(table)



    content.append(
        Spacer(1,40)
    )


    # ===============================
    # تحليل الذكاء الاصطناعي
    # ===============================


    content.append(
        Paragraph(
            "تحليل الذكاء الاصطناعي",
            heading_style
        )
    )


    analysis_text = analysis.replace(
        "\n",
        "<br/>"
    )


    content.append(

        Paragraph(

            analysis_text,

            normal_style

        )

    )


    # ===============================
    # Build PDF
    # ===============================


    doc.build(
        content
    )


    print(
        "PDF Report Created Successfully:"
    )

    print(
        os.path.abspath(file_path)
    )