import google.generativeai as genai
from secret_key import google_api_key

# Configure the GenAI client with your API key
genai.configure(api_key=google_api_key)

def generate_restaurant_name_and_items(cuisine):
    # Initialize the Generative Model
    model = genai.GenerativeModel('gemini-pro')

    # Chain 1: Generate Restaurant Name
    restaurant_name_prompt = (
        f"I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    restaurant_name_response = model.generate_content(
        restaurant_name_prompt,
        generation_config=genai.types.GenerationConfig(temperature=0.7)
    )
    restaurant_name = restaurant_name_response.text.strip()

    # Chain 2: Generate Menu Items
    menu_items_prompt = (
        f"Suggest some menu items for {restaurant_name}. Return it as a comma-separated string."
    )
    menu_items_response = model.generate_content(
        menu_items_prompt,
        generation_config=genai.types.GenerationConfig(temperature=0.7)
    )
    menu_items = menu_items_response.text.strip()

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }


if __name__ == "__main__":
    response = generate_restaurant_name_and_items("Italian")
    print(response)