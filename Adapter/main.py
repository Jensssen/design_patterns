class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    This method is the one that lives on the "right" side of the adapter.
    """

    def request(self, a, b) -> str:
        return f"Target Request: ({a}, {b})"



class Adaptee:
    """
    This class defines a specific version of the request called specific_request.
    As an example, this could be a function in an old library.
    It takes two parameters as an input (a and c).
    Assume that this makes the function incompatible with our existing client code.
    We can not change the specific_request function because it is located in 3rd party lib.
    The Adaptee needs some adaptation before we can use it.
    """

    def specific_request(self, a, c) -> str:
        return f"Adaptee: specific_request ({a}, {c})"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self, a, b) -> str:
        """
        Here we have created an Adapter (the request function) that looks exactly like our client interface and
        it calls the specific_request function in a way that makes it compatible to our code base.
        In our code we can still pass (1,2) to the request function and adjust the
        """
        return f"Adapter: (TRANSLATED) {self.specific_request(b, a)}"


if __name__ == "__main__":
    # Here we execute the default behaviour.
    # We pass the target object that will execute the request method of our target class
    target = Target()
    print(target.request(a=1, b=2))
    print("\n")

    # Here we create an object of the Adaptee class that contains a specific implementation
    # of the target request function.
    adaptee = Adaptee()
    print(adaptee.specific_request(a=1, c=2))

    # So now we have two different implementations of a request. The idea behind the adapter patter is that we
    # implement an adapter that firts of all enables us to call the specific request method but in addition does not
    # require us to change our way of calling the request method.

    # This Adapter has the interface of the Target class but calls the specific request method under the hood.
    adapter = Adapter()
    print(adapter.request(a=1, b=2))
