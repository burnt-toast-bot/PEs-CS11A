# define a function that takes two arguments a size and a message
# defaults to size large and the message 'I love Python'
def make_shirt(size='large', message='I love Python'):
    # prints a statement about the size and the message
    print(f"The shirt with be size {size} and will have the message '{message}' printed on it.")

# makes a shirt size small with the message 'Hello world!'
make_shirt("small", "Hello world!")
# makes shirt with the default arguments
make_shirt()
# makes a shirt sized medium with the default message
make_shirt('medium',)
# makes a shirt sized medium with the message 'A different message'
make_shirt('medium', "A different message")
