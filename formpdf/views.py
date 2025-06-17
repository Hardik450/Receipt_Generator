from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
import datetime
from django.core.mail import EmailMessage
import random


def form_view(request):
    if request.method == 'POST':
        # Buyer and transaction details
        buyer_name = request.POST.get('buyer_name')
        buyer_email = request.POST.get('buyer_email')
        buyer_address = request.POST.get('buyer_address')
        transaction_id = request.POST.get('transaction_id')
        date = request.POST.get('date')

        # Product list
        product_names = request.POST.getlist('product_name[]')
        quantities = request.POST.getlist('quantity[]')
        unit_prices = request.POST.getlist('unit_price[]')
        taxes = request.POST.getlist('tax[]')

        items = []
        subtotal = 0
        total_tax = 0

        for i in range(len(product_names)):
            name = product_names[i]
            qty = int(quantities[i])
            price = float(unit_prices[i])
            tax_percent = float(taxes[i])
            item_total = qty * price
            item_tax = item_total * (tax_percent / 100)

            items.append({
                'name': name,
                'quantity': qty,
                'price': price,
                'tax_percent': tax_percent,
                'total': item_total,
                'tax': item_tax,
                'total_with_tax': item_total + item_tax
            })

            subtotal += item_total
            total_tax += item_tax

        grand_total = subtotal + total_tax

        context = {
            'buyer_name': buyer_name,
            'buyer_email': buyer_email,
            'buyer_address': buyer_address,
            'transaction_id': transaction_id,
            'date': date or datetime.date.today().strftime('%Y-%m-%d'),
            'items': items,
            'subtotal': subtotal,
            'total_tax': total_tax,
            'grand_total': grand_total,
        }
        invoice_number = f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(10,99)}"
        context['invoice_number'] = invoice_number
        # Render PDF
        template = get_template('pdf_template.html')
        html = template.render(context)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

        if not pdf.err:
            # Create the email
            email = EmailMessage(
                subject='Your Receipt from [Your Company]',
                body='Thank you for your purchase. Please find the receipt attached.',
                from_email='yourcompany@example.com',
                to=[buyer_email],  # You must get this from the form
                )
            email.attach('receipt.pdf', response.getvalue(), 'application/pdf')
            email.send()

            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error generating PDF", status=500)

    return render(request, 'form.html')