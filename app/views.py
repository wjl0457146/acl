from app import app
from flask import render_template, request, redirect, url_for
from models import Acl, AclForm
from datetime import datetime


@app.route('/')
def index():
     return redirect(url_for('view_acls',page=1))



@app.route('/add', methods=['POST'])
def add():
    form = AclForm(request.form)
    if form.validate():
        srcip = form.srcip.data
        dstip = form.dstip.data
        dstport = form.dstport.data
        device = form.device.data
        reason = form.reason.data
        staff = form.staff.data
        acl = Acl(srcip=srcip, dstip=dstip, dstport=dstport, device=device, reason=reason, staff=staff, time=datetime.now())
        acl.save()
    paginated_acls = Acl.objects.order_by('-time').paginate(page=1, per_page=10)
    return render_template("index1.html", paginated_acls=paginated_acls, form=form, page=1)

@app.route('/delete/<string:acl_id>')
def delete(acl_id):
    form = AclForm()
    acl = Acl.objects.get_or_404(id=acl_id)
    acl.delete()
    paginated_acls = Acl.objects.order_by('-time').paginate(page=1, per_page=10)
    return render_template("index1.html", paginated_acls=paginated_acls, form=form, page=1)

@app.route('/<int:page>')
def view_acls(page=1):
    form = AclForm()
    paginated_acls = Acl.objects.order_by('-time').paginate(page=1, per_page=10)
    return render_template("index1.html", paginated_acls=paginated_acls, form=form, page=page)


