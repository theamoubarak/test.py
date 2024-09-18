import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="% of Men vs Women in Lebanon")
st.title("Demography Distribution according to Gender and Age in Lebanon")
st.write("Lebanon's demographic landscape is characterized by a relatively balanced gender distribution, with women comprising about 50.4% of the population and men approximately 49.6%. With a total population of around 4.6 million, this slight predominance of women reflects broader regional trends and plays a significant role in shaping the country's social and economic dynamics.")


df = pd.read_csv("datas.csv")

######My interactive plotly bar chart 
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

data = {
    'Percentage of Men': [30, 40, 50, 60, 70],
    'Percentage of Women': [70, 60, 50, 40, 30],
    'Town': ['Town A', 'Town B', 'Town C', 'Town D', 'Town E']
}

df = pd.read_csv("datas.csv")

x_axis_option = st.selectbox("Select the X-axis:", ['Percentage of Men', 'Percentage of Women'])
y_axis_option = st.selectbox("Select the Town:", df['Town'].unique())

st.title(f"Interactive Plotly Bar Chart: {x_axis_option} for {y_axis_option}")

fig = go.Figure()

# Highlight the selected town
selected_town_data = df[df['Town'] == y_axis_option]

# Add a bar trace for the selected town
fig.add_trace(go.Bar(
    x=[y_axis_option],  # Single bar for the selected town
    y=selected_town_data[x_axis_option].values,
    text=selected_town_data[x_axis_option].values,
    textposition='outside',  # Positioned outside the bar for better visibility
    marker=dict(
        color='grey',
        line=dict(width=2, color='DarkSlateGrey')
    ),
    width=0.4,  # Make the bar thinner
    hoverinfo='text'
))

# Update layout dynamically
fig.update_layout(
    title={
        'text': f'Bar Chart: {x_axis_option} for {y_axis_option}',
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 20},
        'pad': {'b': 20}  # Add space below the title
    },
    xaxis_title='Town',
    yaxis_title=x_axis_option,
    xaxis=dict(
        tickmode='array',
        tickvals=[y_axis_option],
        ticktext=[y_axis_option],
        range=[-0.5, 0.5],  # Center the bar on the plot
        showgrid=False,
        showline=True,
        linecolor='black'
    ),
    yaxis=dict(
        title_standoff=20,
        showgrid=True,
        gridcolor='lightgray',
        showline=True,
        linecolor='black',
        zeroline=False,
        ticksuffix='%',
        range=[0, 100]  # Fixed range from 0 to 100%
  # Fixed range for y-axis
    ),
    margin=dict(l=40, r=20, t=60, b=40),  # Increased top margin to add space
    width=400,  # Set the width of the plot
    height=300,  # Set the height of the plot
    plot_bgcolor='white'
)

# Render the plot
st.plotly_chart(fig, use_container_width=True)

st.write("Here's an interactive Plotly bar chart displaying the % of men and/or women by town allowing users to visualize and compare gender distribution across different locations dynamically. By selecting a specific town, the chart updates to reflect the gender proportion for that area, offering an intuitive way to explore demographic data. This feature enhances user engagement and facilitates deeper insights into regional gender patterns.")



st.title("Interactive Bubble Chart showing the % of Elderly and Youth among women within the Lebanese Towns")
########my interactive bubble chart
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Load the dataset
path = "https://linked.aub.edu.lb/pkgcube/data/6ccc6616fbb484c599a4cc560b934c25_20240906_090000.csv"
df = pd.read_csv(path)

# Drop unnecessary columns
df.drop(columns=["publisher", "dataset", "references", "Observation URI"], inplace=True)

# Clean the 'refArea' column by extracting the last part after the last slash
df['refArea'] = df['refArea'].apply(lambda x: x.split('/')[-1])

# Clean column names by removing leading/trailing spaces
df.columns = df.columns.str.strip()

# Convert relevant columns to numeric values
df['Percentage of Eldelry - 65 or more years'] = pd.to_numeric(df['Percentage of Eldelry - 65 or more years'], errors='coerce')
df['Percentage of Youth - 15-24 years'] = pd.to_numeric(df['Percentage of Youth - 15-24 years'], errors='coerce')
df['Percentage of Women'] = pd.to_numeric(df['Percentage of Women'], errors='coerce')

# Get unique refArea values and setup the slider
ref_areas = df['refArea'].unique()
selected_index = st.slider("Select refArea", 0, len(ref_areas) - 1, 0)
selected_ref_area = ref_areas[selected_index]

# Display the selected refArea
st.write(f"Currently viewing data for: *{selected_ref_area}*")

# Filter data based on selected refArea
filtered_df = df[df['refArea'] == selected_ref_area]

# Adjust bubble size (optional: scale down size for better visualization)
bubble_size = filtered_df['Percentage of Women'] / 2  # Scale down the bubble size

# Prepare data for bubble chart
x = filtered_df['Percentage of Eldelry - 65 or more years']  # X-axis: Percentage of Elderly
y = filtered_df['Percentage of Youth - 15-24 years']         # Y-axis: Percentage of Youth
size = bubble_size
text = filtered_df['Town']  # Display Town when hovering

# Create the bubble chart
p3 = go.Scatter(
    x=x, 
    y=y, 
    mode='markers', 
    marker=dict(
        size=size, 
        opacity=0.6, 
        color=size, 
        colorscale='Viridis', 
        colorbar=dict(title='Percentage of Women')
    ), 
    text=text  # Display Town when hovering
)

# Layout of the chart
layout = go.Layout(
    title=f'Bubble Chart for {selected_ref_area}: Percentage of Elderly vs Youth Population with Percentage of Women',
    xaxis_title='Percentage of Elderly (65 or more years)',
    yaxis_title='Percentage of Youth (15-24 years)',
    showlegend=False
)

# Create the figure
fig = go.Figure(data=[p3], layout=layout)

# Plot the figure in Streamlit
st.plotly_chart(fig)

st.write("The bubble chart illustrates the distribution of elderly and youth within the Lebanese population, showcasing the proportion of these age groups in a visually engaging manner. Each bubble represents a different age group, with its size corresponding to the percentage of that group within the total population. The chart provides a clear comparison between the youth and elderly demographics, helping to highlight potential trends, such as aging population concerns or the dominance of younger age groups. This visualization offers insights into how these segments contribute to Lebanon’s demographic structure and could influence policy and resource allocation.")