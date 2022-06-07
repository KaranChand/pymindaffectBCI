
from MultiPage import MultiPage
from pages import data_upload, new_dataset_uploaded_pipeline, new_analysis_method_committed_pipeline

app = MultiPage()

# # Title of the main page
# display = Image.open('MindAffect_Logo.png')
# display = np.array(display)
# # st.image(display, width = 400)
# col1, col2 = st.columns(2)
# col1.image(display, width = 400)
# col2.title("Tracking Dashboard")

app.add_page("Upload file", data_upload.app)
app.add_page("New dataset uploaded pipeline", new_dataset_uploaded_pipeline.app)
app.add_page("New analysis method committed pipeline", new_analysis_method_committed_pipeline.app)

app.run()
