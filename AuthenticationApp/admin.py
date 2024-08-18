from django.contrib import admin
from django.http import HttpResponse
from .models import TmcsMember
from reportlab.lib.pagesizes import landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def download_pdf(modeladmin, request, queryset):
    # Fetch all members
    all_members = TmcsMember.objects.all()

    # Set A1 paper size and orientation
    page_size = (1310, 1500)

    # Set a fixed width for the table (adjust the value as needed)
    table_width = 1310

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="members_report.pdf"'

    # Use ReportLab to generate PDF content
    doc = SimpleDocTemplate(response, pagesize=(landscape(page_size)), rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    elements = []

    # Table header (manually specified fields excluding Password and Last Login)
    table_header = [
        'ID', 'First Name', 'Middle Name', 'Last Name', 'Gender', 'Simu',
        'Student Email Yako', 'Simu', 'Ubatizo', 'Kipaimara', 'Daraja', 'Elimu Uliyonayo',
        'Parokia', 'Jimbo', 'Course', 'Department', 'College', 'Level Unayosoma',
        'Utume Vinginevyo', 'Is Active', 'Is Staff', 'Is Superuser',
        'Is Mwenyekiti Tawi', 'Is Katibu Tawi', 'Is Mhazini Tawi',
        'Is Mwenyekiti Legio', 'Is Katibu Legio', 'Is Mhazini Legio',
        'Is Mwenyekiti Kwaya', 'Is Katibu Kwaya', 'Is Mhazini Kwaya',
        'Is Mwenyekiti Karismatiki', 'Is Katibu Karismatiki', 'Is Mhazini Karismatiki'
    ]

    data = [table_header]

    # Table data
    for member in all_members:
        row_data = [
            member.pk, member.first_name, member.middle_name, member.last_name,
            member.gender, member.namba_ya_mwanafunzi, member.email, member.namba_ya_mzazi, member.ubatizo, member.kipaimara,
            member.ndoa_au_daraja, member.elimu_uliyonayo, member.parokia, member.jimbo_kuu,
            member.course, member.department, member.college, member.level_of_study,
            member.vyama_vya_kitume, member.vinginevyo, member.is_active, member.is_staff,
            member.is_superuser, member.is_mwenyekiti_tawi, member.is_katibu_tawi,
            member.is_mhazini_tawi, member.is_mwenyekiti_legio, member.is_katibu_legio,
            member.is_mhazini_legio, member.is_mwenyekiti_kwaya, member.is_katibu_kwaya,
            member.is_mhazini_kwaya, member.is_mwenyekiti_karismatiki,
            member.is_katibu_karismatiki, member.is_mhazini_karismatiki
        ]

        # Convert long text to a multiline paragraph
        for i, value in enumerate(row_data):
            if len(str(value)) > 15:  # You can adjust the threshold as needed
                row_data[i] = Paragraph(str(value), getSampleStyleSheet()['Normal'])

        data.append(row_data)

    # Create the table with fixed width
    table = Table(data, colWidths=[table_width / len(table_header)] * len(table_header))

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8),  # Adjust font size
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),  # Add inner grid lines
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),  # Add outer border
    ])

    table.setStyle(style)
    elements.append(table)

    # Build the PDF
    doc.build(elements)
    return response

download_pdf.short_description = "Download PDF for all members"


@admin.register(TmcsMember)
class TmcsMembersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'gender','namba_ya_mwanafunzi', 'email', 'namba_ya_mzazi','ubatizo', 'kipaimara', 'ndoa_au_daraja','elimu_uliyonayo', 'parokia', 'jimbo_kuu','course', 'years_of_study', 'department', 'college', 'level_of_study','vyama_vya_kitume','vinginevyo','is_active','is_staff' ,'is_kiongozi_wa_darasa' ,'is_superuser','is_mhazini_tawi','is_mwenyekiti_tawi','is_katibu_tawi','is_mhazini_legio','is_mwenyekiti_kwaya','is_mhazini_kwaya')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender', 'ubatizo', 'kipaimara', 'ndoa_au_daraja','level_of_study', 'vyama_vya_kitume')
    actions = [download_pdf]