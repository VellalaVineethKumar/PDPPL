def get_regulation_and_industry_for_loader() -> tuple[str, str]:
    """Map session state values to correct regulation directory and industry filename for questionnaire loading.

    Returns:
        tuple[str, str]: (regulation_directory, industry_filename)
    """
    import streamlit as st
    industry_file_map = {
        "Oil and Gas": "Oil_and_Gas",
        "Banking and finance": "Banking and finance",
        "E-commerce": "E-commerce"
    }
    regulation_map = {
        "India": "DPDP",
        "Qatar": "PDPPL"
    }
    
    # Get the selected country and regulation
    selected_country = st.session_state.get('selected_country', '')
    regulation = regulation_map.get(selected_country, st.session_state.get('selected_regulation', ''))
    
    # Get the selected industry and ensure it's valid
    selected_industry = st.session_state.get('selected_industry', '')
    if selected_industry == "general" or not selected_industry:
        # Set default industry based on country
        if selected_country == "Qatar":
            selected_industry = "Oil and Gas"
        elif selected_country == "India":
            selected_industry = "Banking and finance"
        else:
            selected_industry = "Oil and Gas"  # Default fallback
    
    # Map the display industry to file industry
    industry = industry_file_map.get(selected_industry, selected_industry)
    
    return regulation, industry 