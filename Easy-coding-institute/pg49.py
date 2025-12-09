text="""At our organization, customer obsession is the element of Day 1 culture that matters most to our success. 
By putting our customers at the forefront of every decision, 
we've achieved a 25% increase in customer satisfaction scores and a 15% increase in customer retention rates. 
This customer-centric approach has not only driven business growth but also fostered a culture of innovation and continuous improvement."""

words = text.split(' ')

for word in words:
    if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
        
        print(word.replace(",",""))