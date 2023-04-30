from django.views import generic
from django.urls import reverse_lazy
from reportlab.lib import colors
from .models import User, Invoice, Product
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'


class DashboardView(generic.TemplateView):
    template_name = 'core/dashboard.html'


class InvoicesListView(generic.ListView):
    model = Invoice
    template_name = 'core/invoice/invoices_list.html'
    context_object_name = 'invoices_list'

    def get_queryset(self):
        return Invoice.objects.all()


class InvoiceDetailView(generic.DetailView):
    model = Invoice
    template_name = 'core/invoice/invoice_detail.html'
    context_object_name = 'invoice'


class InvoiceAdd(generic.CreateView):
    model = Invoice
    fields = [
        'seller',
        'purchaser',
        'products',
        'invoice_number',
        'sale_date',
        'date_of_issue',
    ]
    template_name = 'core/invoice/invoice_add.html'
    success_url = reverse_lazy('core:invoices_list')


class InvoiceUpdate(generic.UpdateView):
    model = Invoice
    fields = [
        'seller',
        'purchaser',
        'products',
        'invoice_number',
        'sale_date',
        'date_of_issue',
    ]
    template_name = 'core/invoice/invoice_update.html'
    success_url = reverse_lazy('core:invoices_list')


class InvoiceDelete(generic.DeleteView):
    model = Invoice
    template_name = 'core/invoice/invoice_confirm_delete.html'
    success_url = reverse_lazy('core:invoices_list')


class ProductsListView(generic.ListView):
    model = Product
    template_name = 'core/product/products_list.html'
    context_object_name = 'products_list'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'core/product/product_detail.html'
    context_object_name = 'product'


class ProductAdd(generic.CreateView):
    model = Product
    fields = [
        'name',
        'description',
        'net_price',
        'tax_rate',
        'gross_price',
        'amount'
    ]
    template_name = 'core/product/product_add.html'
    success_url = reverse_lazy('core:products_list')


class ProductUpdate(generic.UpdateView):
    model = Product
    fields = [
        'name',
        'description',
        'net_price',
        'tax_rate',
        'gross_price',
        'amount'
    ]
    template_name = 'core/product/product_update.html'
    success_url = reverse_lazy('core:products_list')


class ProductDelete(generic.DeleteView):
    model = Product
    template_name = 'core/product/product_confirm_delete.html'
    success_url = reverse_lazy('core:products_list')


class UsersListView(generic.ListView):
    model = User
    template_name = 'core/user/users_list.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'core/user/user_detail.html'
    context_object_name = 'user'


class UserAdd(generic.CreateView):
    model = User
    fields = [
        'email',
        'first_name',
        'last_name',
        'street_address',
        'city',
        'country',
        'postal_code',
        'contact_information',
        'account_status',
    ]
    template_name = 'core/user/user_add.html'
    success_url = reverse_lazy('core:users_list')


class UserUpdate(generic.UpdateView):
    model = User
    fields = [
        'email',
        'first_name',
        'last_name',
        'street_address',
        'city',
        'country',
        'postal_code',
        'contact_information',
        'account_status',
    ]
    template_name = 'core/user/user_update.html'
    success_url = reverse_lazy('core:users_list')


class UserDelete(generic.DeleteView):
    model = User
    template_name = 'core/user/user_confirm_delete.html'
    success_url = reverse_lazy('core:users_list')


def generate_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    products = Product.objects.filter(invoice=invoice)
    user = User.objects.get(id=invoice.purchaser.id)

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(colors.black)

    pdf.setFont('Helvetica-Bold', 16)
    pdf.drawString(1 * inch, 10.5 * inch, 'Invoice')
    pdf.setFont('Helvetica', 12)
    pdf.drawString(1 * inch, 10.25 * inch, user.country)
    pdf.drawString(1 * inch, 10 * inch, f'{user.city} {user.postal_code}, {user.street_address}')
    pdf.drawString(1 * inch, 9.75 * inch, f'Phone: {user.contact_information}')
    pdf.drawString(1 * inch, 9.5 * inch, f'Email: {user.email}')

    pdf.setLineWidth(1)
    pdf.line(1 * inch, 5.75 * inch, 8 * inch, 5.75 * inch)

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(1 * inch, 9 * inch, 'Item')
    pdf.drawString(3 * inch, 9 * inch, 'Quantity')
    pdf.drawString(4 * inch, 9 * inch, 'Price')
    pdf.drawString(5 * inch, 9 * inch, 'Total')
    pdf.line(1 * inch, 8.9 * inch, 6.5 * inch, 8.9 * inch)

    y = 8.5 * inch
    for product in products:
        pdf.setFont('Helvetica', 12)
        pdf.drawString(1 * inch, y, product.name)
        pdf.drawString(3 * inch, y, str(product.amount))
        pdf.drawString(4 * inch, y, '${:,.2f}'.format(product.gross_price))
        pdf.drawString(5 * inch, y, '${:,.2f}'.format(product.amount * product.gross_price))
        y -= 0.25 * inch

    total = sum(product.amount * product.gross_price for product in products)
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(4 * inch, y - 0.5 * inch, 'Total:')
    pdf.drawString(5 * inch, y - 0.5 * inch, '${:,.2f}'.format(total))

    pdf.showPage()
    pdf.save()

    pdf_name = '%s.pdf' % invoice.invoice_number.replace(' ', '')

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=pdf_name)

