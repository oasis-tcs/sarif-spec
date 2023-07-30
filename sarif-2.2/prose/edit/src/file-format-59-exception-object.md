## exception object

### General{#exception-object--general}

An `exception` object describes a runtime exception encountered during the execution of an analysis tool. This includes signals in POSIX-conforming operating systems

### kind property{#exception-object--kind-property}

An `exception` object **SHOULD** contain a property named `kind` whose value is a string describing the exception.

If the exception represents a thrown object, `kind` **SHALL** be the fully qualified type name of the object that was thrown, if that information is available.

> EXAMPLE 1: C#: `"System.ArgumentNullException"`

If the exception represents a POSIX signal, `kind` **SHALL** be the symbolic name of the signal as specified in `<signal.h>`.

> EXAMPLE 2: POSIX: `"SIGFPE"`

If the tool does not have access to information about the object that was thrown, the `kind` property **SHALL** be absent.

### message property{#exception-object--message-property}

An `exception` object **SHOULD** contain a property named `message` whose value is a string that describes the exception.

If the tool does not have access to an appropriate property of the thrown object, the `message` property **SHALL** be absent.

> EXAMPLE 1: C++: The tool might populate `message` with the string returned from the `what()` method of any object derived from `std::exception`.

> EXAMPLE 2: C#: The tool might populate `message` with the value returned from the `ToString()` method of the `System.Exception` object, or (less informatively) from that object’s `Message` property.

### stack property{#exception-object--stack-property}

An `exception` object **MAY** contain a property named `stack` whose value is a `stack` object ([§3.44](#stack-object)) that describes the sequence of function calls leading to the exception.

### innerExceptions property

An `exception` object **MAY** contain a property named `innerExceptions` whose value is an array of zero or more `exception` objects each of which is considered a cause of the containing exception.

> NOTE: There is commonly no more than one inner exception. This property is an array to accommodate platforms that provide a mechanism for aggregating exceptions, such as the `System.AggregateException` class from the .NET Framework.
