import os


def find_nearest_parent(
        parent_name: str, current_path: str = os.getcwd(), sep: str = os.sep
) -> str | None:
    """
    Find the nearest parent directory matching the given parent_name.

    Args:
        parent_name (str): The name of the parent directory to find.
        current_path (str): The starting path.
        sep (str): separating char, \ or /.

    Returns:
        str: Full path of the matching parent directory, or None if not found.
    """
    # Split the current path into its components
    components = current_path.split(sep)
    print(current_path)
    print(components)

    # Check if the parent_name exists in the components
    if parent_name in components:
        # Reconstruct the path up to the matching parent
        index = components.index(parent_name)
        return sep.join(components[: index + 1])
    else:
        return None
