heros=['spiderman', 'thor', 'hulk', 'iron man', 'captain america']
#1. Length of the list
print('Length of list is ', len(heros))
#2. Add 'black panther' at the end of this list
heros.append('Black panther')
print('List after adding black panther :', heros)
#3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3, 'black panther')
print('List after adding black panther after hulk:', heros)
#4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
heros[1:3]=['doctor strange']
print('List after replacing thor and hulk with doctor strange', heros)
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print(heros.sort())
