from django.shortcuts import get_object_or_404, render

from .models import ChaiVarietie,Store
from .forms import ChaiVarietieForm
# Create your views here.  
def all_chai(request):
    chai_varieties = ChaiVarietie.objects.all() # pylint: disable=no-member
    return render(request, 'chai/all_chai.html', {'chai_varieties': chai_varieties})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarietie, id=chai_id)  # pylint: disable=no-member
    return render(request, 'chai/chai_details.html', {'chailol': chai})

def chai_stores(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietieForm(request.POST)
        if form.is_valid():
            chai_varieties = form.cleaned_data['chai_varieties']  
            stores = Store.objects.filter(chai_varieties=chai_varieties)  # pylint: disable=no-member
    else:
        form = ChaiVarietieForm()
    return render(request, 'chai/chai_stores.html', {'stores': stores,'form': form})