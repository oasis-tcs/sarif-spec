## rectangle object

### General{#rectangle-object--general}

A `rectangle` object specifies a rectangular area within an image. When a SARIF viewer displays an image, it **MAY** indicate the presence of these areas, for example, by highlighting them or surrounding them with a border.

### top, left, bottom, and right properties

A `rectangle` object **SHALL** contain properties named `top`, `left`, `bottom`, and `right`, each of which contains a number (as defined by the JSON Schema standard \[[JSCHEMA01](#JSCHEMA01)\]) specifying one of the coordinates of the rectangle within the image. These properties **SHALL** be measured in the image format’s natural units (for example, pixels for raster-based image formats). These values **MAY** be positive or negative, depending on the natural coordinate system of the image format. They **MAY** increase either from left to right or from right to left, and either from top to bottom or from bottom to top, again depending on the natural coordinate system of the image format.

> NOTE: A number in JSON schema can take a variety of forms, including simple integers (`42`) and floating-point numbers (`3.14`).

### message property{#rectangle-object--message-property}

A `rectangle` object **SHOULD** contain a property named `message` whose value is a `message` object ([§3.11](#message-object)) containing a message relevant to this area of the image.

A SARIF viewer **MAY** display this message when the user interacts with the area. For example, if the user hovers over the area with the mouse, the viewer might present the message as hover text.
