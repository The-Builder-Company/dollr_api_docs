---
title: "Glossary"
description: "Definitions for key terms used throughout the Dollr API."
---

# Glossary

Definitions for all key terms used across the Dollr API.

---

## A

**Access Token**
A short-lived JWT Bearer token obtained via `POST /v1/jwt/client/obtain/token`. Must be included in the `Authorization: Bearer <token>` header on every protected API call. Expires after the number of minutes specified in `expires_in`.

**AIRTEL_RWA**
Payment method and provider identifier for Airtel Money in Rwanda. Routed via PawaPay.

**Amount**
All monetary amounts in the API are positive numbers. Minimum value is `0.01` for decimal currencies and `1` for integer currencies. Amounts in prediction and execution responses may differ between payer and payee depending on the fee bearer setting.

---

## C

**Canceled**
A terminal document status. An invoice or order that has been canceled cannot be reactivated or paid. Triggered by calling the cancel endpoint.

**Client Credentials**
A `client_id` and `client_secret` pair generated in the Merchant Portal under **Settings → Developer → API Keys**. Used to obtain Bearer tokens via the OAuth 2.0 Client Credentials flow. The `client_secret` is shown only once — store it securely.

**Collection**
An operation type where funds flow *into* your merchant wallet from a customer. Initiated via a checkout session and executed via `POST /v1/executions/collection`.

<span id="counterparty">**Counterparty**</span>
A record that links an existing [Party](#party) to your merchant account with a defined [relationship type](#relationship-type). For the direct invoice and order flows in these docs, a counterparty is required before creating invoices or orders. Checkout-source creation (`POST /v1/checkouts/create`) can create or match the Party and Counterparty automatically. A counterparty answers "who is this party to me?" (customer, supplier, employee, etc.).

**CREDIT_CARD**
Payment method identifier for international credit and debit card payments.

**Currency**
All currency codes follow ISO 4217 — three uppercase letters (e.g., `USD`, `LRD`, `RWF`). Liberian Dollar (`LRD`) and US Dollar (`USD`) are the primary currencies in Liberia. Rwandan Franc (`RWF`) is used in Rwanda.

---

## E

<span id="execution">**Execution**</span>
The API call that triggers actual movement of funds. Executions require an active [Session](#session) and a unique [Reference ID](#reference-id). Four execution types exist: `COLLECTION`, `PAYOUT`, `TRANSFER`, `REFUND`. See the [Executions](../api/executions.md) page.

**ExecutionResponse**
The response object returned by all execution and status endpoints. Contains `reference_id`, `status`, `operation_type`, `payer_amount`, `payee_amount`, `provider_transaction_id`, and gateway/wallet messages.

**expires_in**
For Bearer tokens: the number of **minutes** until the token expires. For Realtime Keys: the number of **seconds** until the token expires.

---

## F

**Fee Bearer**
Controls who absorbs transaction fees:

- **`PAYER`** — The customer pays fees on top of the invoice total. The merchant receives the full invoiced amount.
- **`PAYEE`** — The merchant absorbs the fees. The customer pays the invoice total; the merchant receives less after deductions.

**FX Fee**
A foreign exchange conversion fee charged when the payer's currency differs from the payee's currency. Visible in prediction and receipt responses as `fx_fee`.

---

## G

**Gateway Fee**
A fee charged by the payment gateway per transaction. Varies by payment method and operation type. Query current rates via `GET /v1/fees/gateway`.

**Gateway Provider**
The underlying payment network that processes a transaction. See [Provider](#provider) below.

---

## I

**IDLE**
The initial status of a newly created invoice or order. While `IDLE`, the document can be edited and line items can be added or removed. Publishing transitions the document to `ACTIVE`.

**Idempotency Key**
See [Reference ID](#reference-id).

**Invoice**
A formal billing document with an auto-generated invoice number (`INV-YYYY-NNNNN`), an optional due date, and line items. Follows the lifecycle: `IDLE → ACTIVE → PROCESSING → PAID / CANCELED`. See [Invoices](../api/invoices.md).

**ISO 4217**
The international standard for currency codes. All currency values in the Dollr API use 3-letter ISO 4217 codes in uppercase.

**ISO 8601**
The international standard for date and time representation. All timestamps in the Dollr API use ISO 8601 format, e.g., `2025-06-01T14:30:00Z`.

---

## K

**KYB (Know Your Business)**
Business identity verification required for registered companies and organizations. Part of the Dollr merchant onboarding process.

**KYC (Know Your Customer)**
Individual identity verification. Required for sole proprietors and the designated contact person of registered businesses.

---

## M

**MICRO_ORGANIZATION**
An owner type representing a sole proprietorship or unregistered business. Used in fee tier queries, merchant info, and session parameters.

**MMO (Mobile Money Operator)**
A mobile network operator that provides mobile wallet services. Examples: MTN, Orange, Airtel. The Dollr API supports MMOs across Liberia and Rwanda.

**MTN_MOMO_LBR**
Payment method identifier for MTN Mobile Money in Liberia. Routed via PawaPay.

**MTN_MOMO_RWA**
Payment method identifier for MTN Mobile Money in Rwanda. Routed via PawaPay.

---

## O

**Operation Type**
Describes the direction and nature of a transaction:

| Type | Description |
|---|---|
| `COLLECTION` | Collect funds from a customer into your wallet |
| `PAYOUT` | Send funds from your wallet to a recipient |
| `TRANSFER` | Move funds between Dollr wallets |
| `REFUND` | Return funds from a completed collection |

**Order**
An informal payment document without a formal invoice number or due date. Suited for retail and e-commerce. Follows the same lifecycle as invoices. See [Orders](../api/orders.md).

**ORANGE_MONEY_LBR**
Payment method identifier for Orange Money in Liberia. Routed via PawaPay.

**ORANGE_MONEY_RWA**
Payment method identifier for Orange Money in Rwanda. Routed via PawaPay.

**ORGANIZATION**
An owner type representing a formally registered company or NGO. Requires KYB verification.

---

## P

**PAID**
A terminal document status. The invoice or order has been successfully paid. A receipt is available after this state is reached.

<span id="party">**Party**</span>
A contact record representing a person or entity — identified by name, phone number, and optionally email and country code. Parties are the people your business transacts with. A Party becomes meaningful in context through a [Counterparty](#counterparty) relationship. See [Parties](../api/parties.md).

**PAWAPAY**
The payment gateway that routes mobile money transactions across Africa. Dollr uses PawaPay for MTN Mobile Money, Orange Money, and Airtel Money across Liberia and Rwanda.

**Payment Account**
A record binding a specific account number (mobile wallet, card) to a Party and payment method. Required before executing a collection or payout. See [Payment Accounts](../api/payment-accounts.md).

**Payment Link**
An invoice or order shared via URL that customers can pay directly in a browser — without a Dollr account. Enabled by setting `as_payment_link: true` when creating an invoice or order.

**PAYEE**
The party *receiving* funds. In the context of fee bearer: when `fee_bearer` is `PAYEE`, the merchant (payee) absorbs the transaction fees.

**PAYER**
The party *sending* funds. In the context of fee bearer: when `fee_bearer` is `PAYER`, the customer pays fees on top of the invoice total.

**Platform Fee**
A fee charged by Dollr for processing the transaction. Rates vary by fee tier. Query current rates via `GET /v1/fees/platform`.

**PLATFORM**
Provider identifier for internal Dollr wallet transfers. No external gateway involved.

**PROCESSING**
An intermediate document or execution status. Funds movement has been initiated but the payment provider has not yet confirmed the result. Mobile money transactions may remain in this state for several minutes. Do not cancel or retry during this window.

<span id="provider">**Provider**</span>
The payment network or gateway routing the transaction. Note: `provider` identifies the routing network (for example `PAWAPAY`, `STRIPE`, `PLATFORM`), while `payment_method` identifies the instrument used (for example `MTN_MOMO_LBR`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`). Keep these concepts distinct when mapping examples and request fields.

| Provider | Description |
|---|---|
| `PAWAPAY` | Mobile money gateway (MTN, Orange, Airtel) |
| `STRIPE` | International card processing |
| `PLATFORM` | Internal Dollr wallet balance |

---

## R

**Realtime Key**
A short-lived token (expires in seconds) used to subscribe to live payment status push updates for an active checkout session. Eliminates the need to poll `GET /v1/status/*`. See [Realtime Keys](../api/realtime-keys.md).

**Receipt**
A post-payment document available once an invoice or order reaches `PAID` status. Contains the full fee breakdown, FX rate, provider transaction ID, and line items.

<span id="reference-id">**Reference ID**</span>
A UUID v4 string you generate and supply with every execution call. This is your **idempotency key** — it identifies the transaction uniquely in Dollr's system. If a network error occurs, query `GET /v1/status/{type}/{reference_id}` with the original reference ID before generating a new one and retrying. Never reuse a reference ID for a different transaction.

**Refund**
An operation that returns funds to a customer from a previously completed collection. Requires creating a refund session with the original `payment_intent_id` and then executing via `POST /v1/executions/refund`.

<span id="relationship-type">**Relationship Type**</span>
Describes how a counterparty relates to your merchant account:

`CUSTOMER` `SUPPLIER` `EMPLOYEE` `FRIEND` `FAMILY` `DONOR` `DONEE` `CONTACT` `SERVICE_PROVIDER` `PARTNER` `BENEFICIARY`

---

## S

<span id="session">**Session**</span>
Declares payment intent before funds move. A session captures what you intend to do (checkout, payout, transfer, refund), with whom, and for how much. Sessions expire if not executed within the specified window. See [Sessions](../api/sessions.md).

**Source Type**
Specifies the type of document backing a checkout session or prediction:

- `INVOICE` — Session is backed by an invoice
- `ORDER` — Session is backed by an order
- `SUBSCRIPTION` — Reserved for future support; not currently documented as a public source family

**STRIPE**
Provider identifier for international credit and debit card payments.

---

## T

**Transfer**
An operation type that moves funds between Dollr wallets — from one merchant wallet to a counterparty's Dollr wallet. No external payment gateway involved.

---

## U

**UUID v4**
A randomly generated universally unique identifier in the format `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`. Required for all `reference_id` fields. Use your language's built-in UUID library — never construct these manually.

---

## V

**Verification**
The compliance process confirming a merchant's identity (KYC for individuals, KYB for businesses). Required before accessing transfers, payouts, API key generation, and refunds.

---

## W

**WALLET**
Payment method identifier for Dollr internal wallet balance. Used for transfers between platform wallets. Provider is `PLATFORM`.

**Wallet**
A Dollr-managed balance account tied to a merchant entity. Wallets hold funds in a specific currency. Statuses: `ACTIVE`, `RESTRICTED`, `FROZEN`, `CLOSED`. Wallets are the source for payout and transfer sessions (`wallet_id`).
