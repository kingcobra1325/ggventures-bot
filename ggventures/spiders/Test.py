testString = "//div[@class='description'] | //div[@class='description']"

method = 'attr' if '//span' in testString else 'text'

print(method)
