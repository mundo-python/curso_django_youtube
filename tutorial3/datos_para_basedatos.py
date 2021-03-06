
java = Lenguaje.objects.create(nombre='java', creador='James Gosling')
c = Lenguaje.objects.create(nombre='c', creador='Dennis Ritchie')
python = Lenguaje.objects.create(nombre='python', creador='Guido van Rossum')
haskell = Lenguaje.objects.create(nombre='haskell')
javascript = Lenguaje.objects.create(nombre='javascript', creador='Brendan Eich')
basic = Lenguaje.objects.create(nombre='basic', creador='John G. Kemeny')
cplusplus = Lenguaje.objects.create(nombre='c++', creador='Bjarne Stroustrup')
csharp = Lenguaje.objects.create(nombre='c#')
swift = Lenguaje.objects.create(nombre='swift', creador='Chris Lattner')
kotlin = Lenguaje.objects.create(nombre='kotlin')

google = Empresa.objects.create(nombre='Google', fundacion=1998)
microsoft = Empresa.objects.create(nombre='Microsoft', fundacion=1975)
apple = Empresa.objects.create(nombre='Apple', fundacion=1975)
amazon = Empresa.objects.create(nombre='Amazon', fundacion=1999)
ebay = Empresa.objects.create(nombre='Ebay', fundacion=1997)
facebook = Empresa.objects.create(nombre='Facebook', fundacion=2004)
twitter = Empresa.objects.create(nombre='Twitter', fundacion=2009)
yahoo = Empresa.objects.create(nombre='Yahoo', fundacion=1996)
snapchat = Empresa.objects.create(nombre='Snapchat', fundacion=2012)
instagram = Empresa.objects.create(nombre='Instagram', fundacion=2010)

Programador.objects.create(nombre='John', edad=22, empresa= apple)
Programador.objects.create(nombre='Juan', edad=22, empresa= apple)
Programador.objects.create(nombre='Jose', edad=25, empresa=twitter)
Programador.objects.create(nombre='Edgar', edad=26, empresa=twitter)
Programador.objects.create(nombre='Mark', edad=26, empresa = facebook)
Programador.objects.create(nombre='Venus', edad=28, empresa=snapchat)
Programador.objects.create(nombre='Sol', edad=28, empresa=snapchat)
Programador.objects.create(nombre='Andrea', edad=29, empresa=yahoo)
Programador.objects.create(nombre='Cardi', edad=23, empresa=amazon)
Programador.objects.create(nombre='Maria', edad=23, empresa=google)
Programador.objects.create(nombre='Joel', edad=24, empresa=google)
Programador.objects.create(nombre='Salman', edad=25, empresa=google)
Programador.objects.create(nombre='Tabata', edad=27, empresa=ebay)
