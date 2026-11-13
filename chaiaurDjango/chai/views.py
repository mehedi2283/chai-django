from django.shortcuts import get_object_or_404, render
from .models import ChaiVarietie

# Create your views here.  
def all_chai(request):
    chai_varieties = ChaiVarietie.objects.all() # pylint: disable=no-member
    return render(request, 'chai/all_chai.html', {'chai_varieties': chai_varieties})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarietie, id=chai_id)  # pylint: disable=no-member
    return render(request, 'chai/chai_details.html', {'chailol': chai})