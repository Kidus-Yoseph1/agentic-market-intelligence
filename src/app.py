import streamlit as st
from main import run

st.set_page_config(page_title="Market Intelligence", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ Market Intelligence Report")
st.markdown("Enter a topic to generate a clean strategy report.")

topic = st.text_input("Analysis Topic:", placeholder="e.g., Autonomous Vehicles")

if st.button("Generate Report", type="primary"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner(f"Agents are researching {topic}..."):
            # Call the function and get the string directly
            report_content = run(topic)
            
            if report_content.startswith("Error:"):
                st.error(report_content)
            else:
                st.success("Analysis Complete!")
                st.divider()
                
                # This displays ONLY the final markdown report
                st.markdown(report_content)
                
                # Add a download button for the clean report
                st.download_button(
                    label="Download as Markdown",
                    data=report_content,
                    file_name=f"report_{topic.lower().replace(' ', '_')}.md"
                )