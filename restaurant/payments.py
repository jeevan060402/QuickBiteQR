"""Placeholder for payment integrations (e.g., Stripe)."""


def create_payment_intent(amount_cents, currency='usd'):
    # TODO: integrate Stripe here. Return a client_secret-like placeholder.
    return {'client_secret': None, 'amount': amount_cents, 'currency': currency}


def verify_webhook(payload, signature):
    # TODO: validate webhook signature
    return False
