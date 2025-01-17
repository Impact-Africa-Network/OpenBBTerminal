"""ECB provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_ecb.models.balance_of_payments import ECBBalanceOfPaymentsFetcher
from openbb_ecb.models.currency_reference_rates import ECBCurrencyReferenceRatesFetcher
from openbb_ecb.models.eu_yield_curve import ECBEUYieldCurveFetcher

ecb_provider = Provider(
    name="ECB",
    website="https://data.ecb.europa.eu",
    description="""The ECB Data Portal provides access to all official ECB statistics.
The portal also provides options to download data and comprehensive metadata for each dataset.
Statistical publications and dashboards offer a compilation of key data on selected topics.""",
    fetcher_dict={
        "BalanceOfPayments": ECBBalanceOfPaymentsFetcher,
        "CurrencyReferenceRates": ECBCurrencyReferenceRatesFetcher,
        "EUYieldCurve": ECBEUYieldCurveFetcher,
    },
    repr_name="European Central Bank (ECB)",
    logo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Logo_European_Central_Bank.svg/720px-Logo_European_Central_Bank.svg.png",  # noqa: E501  pylint: disable=line-too-long
)
