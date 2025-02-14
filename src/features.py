"""Module Imports"""

def get_features(recipes, interactions):
    """
    Select the most important features for modeling.
    Args:
        recipes: DataFrame containing recipes data with engineered features.
        interactions: DataFrame containing user interaction data.
    Returns:
        selected_features: DataFrame containing only selected features.
    """
    #################################
    # Feature Engineering
    #################################

    # Compute average rating per recipe
    avg_rating_per_recipe = (
        interactions.groupby("recipe_id")["rating"].mean().rename("avg_rating")
    )

    # Compute number of interactions per recipe (popularity proxy)
    num_interactions_per_recipe = (
        interactions.groupby("recipe_id").size().rename("num_interactions")
    )

    # Merge the computed features back into the recipes dataset
    recipes = recipes.merge(
        avg_rating_per_recipe, left_on="id", right_index=True, how="left"
    )
    recipes = recipes.merge(
        num_interactions_per_recipe, left_on="id", right_index=True, how="left"
    )

    # Fill missing values (some recipes may not have interactions)
    recipes["avg_rating"].fillna(0)
    recipes["num_interactions"].fillna(0)

    # Filter out recipes with a complexity score over 100 and rating below 4
    recipes = recipes[
        (recipes["avg_rating"] >= 4)
        & (recipes["num_interactions"] >= 3)
    ]

    #################################
    # Feature Selection
    #################################

    # Select the most important features
    selected_columns = [
        "name",
        "avg_rating",
        "minutes",
        "ingredients",
        "steps",
    ]
    selected_features = recipes[selected_columns]

    # Further feature selection logic can be added here

    return selected_features
