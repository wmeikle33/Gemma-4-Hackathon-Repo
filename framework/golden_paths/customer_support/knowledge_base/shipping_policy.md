# Shipping Policy

## Shipping Overview

This document provides general information about shipping, delivery, and order fulfillment. It is intended to help answer common customer questions.

The customer-support workflow may explain shipping policies but must not promise delivery dates, modify orders, or override shipping processes.

## Processing Time

Orders are typically processed before they are shipped.

Processing time may vary depending on:

- Order volume
- Product availability
- Payment verification
- Holidays and weekends
- Warehouse operating hours

Processing time is separate from shipping time.

## Shipping Methods

Available shipping methods may include:

- Standard Shipping
- Expedited Shipping
- Overnight Shipping
- International Shipping

Available options depend on the customer's location and the products being ordered.

The support agent should only describe available shipping methods if that information is provided by an approved source.

## Delivery Estimates

Estimated delivery dates are estimates only.

Actual delivery times may be affected by:

- Weather
- Customs inspections
- Carrier delays
- Incorrect shipping addresses
- Local delivery conditions
- High shipping volume

The support agent must avoid guaranteeing delivery by a specific date unless confirmed by an approved shipping system.

## Tracking Orders

Customers may request the status of a shipment.

If an approved tracking tool is available, the workflow may retrieve:

- Shipment status
- Carrier name
- Tracking number
- Estimated delivery date

If no tracking tool is available, the workflow should explain that shipment status cannot be confirmed automatically.

Example response:

> I cannot verify your shipment status at the moment. Please use the tracking number provided in your shipping confirmation email or contact customer support for assistance.

## Delayed Shipments

If a shipment appears delayed, the support agent should:

1. Explain that shipping estimates are not guaranteed.
2. Recommend checking the tracking information.
3. Suggest waiting for the next carrier update if the package is still in transit.
4. Escalate the request if the delay exceeds company policy or requires investigation.

The workflow should not assume that a package has been lost.

## Lost Packages

Packages that appear to be lost require human review.

The support agent may:

- Explain the investigation process.
- Recommend checking with neighbors or building management.
- Suggest confirming the shipping address.

The workflow must not issue refunds or replacement orders automatically.

## Incorrect Shipping Address

If the customer reports an incorrect shipping address:

- The workflow should not modify the shipping address directly.
- Address changes may only be performed through approved order-management tools.
- If the order has already shipped, address changes may no longer be possible.

Requests requiring address changes should be escalated if necessary.

## International Shipping

International shipments may be affected by:

- Customs processing
- Import duties
- Taxes
- Local regulations
- Carrier restrictions

The support agent should avoid estimating customs processing times.

## Damaged Packages

If a package arrives damaged, the customer should:

1. Keep the packaging.
2. Photograph the damage if requested by company policy.
3. Contact customer support.

Damage claims generally require human review.

The workflow should not approve refunds or replacements automatically.

## Missing Items

If an order arrives with missing items, the workflow should:

1. Ask the customer to review the packing slip.
2. Confirm whether multiple shipments were expected.
3. Escalate the request if the missing item cannot be explained.

## Order Changes

The shipping workflow cannot:

- Cancel shipments
- Modify shipping addresses
- Upgrade shipping methods
- Split shipments
- Change carriers

These requests require an approved order-management workflow or human review.

## Human Review Is Required When

The request should be escalated if:

- A package appears lost.
- A package is damaged.
- Delivery requires investigation.
- The customer requests compensation.
- An address must be changed after an order is placed.
- A carrier dispute exists.
- The shipment requires manual intervention.

## Example Questions

This document may be relevant to questions such as:

- Where is my order?
- When will my package arrive?
- Why hasn't my order shipped yet?
- Can I change my shipping address?
- What shipping methods do you offer?
- My package is delayed.
- My package is lost.
- My package arrived damaged.
- Why hasn't my tracking information updated?
- Do you ship internationally?

## Implementation Note

In the customer-support golden path, shipping information is provided as general policy guidance only.

The example workflow does not connect to a live shipping provider. Shipment status, tracking information, delivery estimates, and order modifications should only be retrieved or performed using approved shipping or order-management tools.
