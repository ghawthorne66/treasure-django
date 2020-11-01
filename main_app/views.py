from django.shortcuts import render


# Create your views here.
def index(request):
  return render(request, 'index.html', {'treasures':treasures})

class Treasure:
  def __init__(self, name, value, material, location, img_url):
      self.name = name
      self.value = value
      self.material = material
      self.location = location
      self.img_url = img_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", "https://www.thermofisher.com/blog/wp-content/uploads/sites/3/2018/03/gold20nugget.jpg"),
    Treasure('Fools Gold', 0, 'Pyrite', "Fools Falls, CO", "https://www.thermofisher.com/blog/wp-content/uploads/sites/3/2018/03/gold20nugget.jpg"),
    Treasure ("Coffee Can", 20.00, 'tin', "Acme, CA", "https://www.thermofisher.com/blog/wp-content/uploads/sites/3/2018/03/gold20nugget.jpg")
]

# "localhost:8000/images/value-icon.png"

  # Treasure ("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO")
  # Treasure ("Coffee Can", 20.00, 'tin', "Acme, CA")

# t1 = Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM")
# t2 = Treasure("Fool's Gold ", 0. 'pyrite', "Fool's Falls, CO")
