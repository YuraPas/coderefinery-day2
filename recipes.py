def scale_amount(amount, base_servings, target_servings):
    if amount < 0:
        raise ValueError("amount must be non-negative")

    if base_servings <= 0:
        raise ValueError("base servings must be positive")

    if target_servings <= 0:
        raise ValueError("target servings must be positive")

    return amount * target_servings / base_servings


if __name__ == "__main__":
    flour = scale_amount(150, 2, 3)
    milk = scale_amount(250, 2, 3)

    print(f"Flour: {flour:g} g")
    print(f"Milk: {milk:g} ml")