import re
import json
import streamlit as st
import pandas as pd

st.title("WALID HAJERI - Customer Engineer Presentation")

# Load CV data (modified for proper JSON formatting)
cv_data = """
{
    "personal": {
        "name": "WALID HAJERI",
        "title": "Cloud/AI Customer Engineer",
        "location": "Paris Region, France",
        "linkedin": "http://www.linkedin.com/in/walidhajeri"
    },
    "objective": "Experienced AI / Cloud Solutions Engineer with over 15 years of experience in the tech/cloud industry.",
    "experience": [
        {
            "years": "2022-present",
            "title": "Principal Cloud Adoption Manager",
            "company": "ORACLE",
            "location": "Paris",
            "responsibilities": [
                "Leading successful onboarding of new customers and workloads, technical advisory, sharing product updates & best practices, mitigating risks, ensuring customer satisfaction Coordinating multiple teams (specialists, product management, etc.) Increased account portfolio usage by 18% in the first year and 39% in the second year",
                "Monitoring & reviewing cloud adoption plans & forecasts for a portfolio of +12€ M ARR top-tier customers (manufacturing/aerospace/retail) Participation in setting-up & standardizing post-sales service catalogue across EMEA Scope: Oracle Cloud Infrastructure PaaS/laas (+ 100 products)"
            ]
        },
        {
            "years": "2018-2022",
            "title": "Principal Customer Success Manager",
            "company": "Axway",
            "location": "Paris",
            "responsibilities": [
                "CSM & Technical Account Management of all-tier cloud accounts across EMEA",
                "Achieved usage increase +8% per year, 110% Retention Rate",
                "Proactively conducted Business Reviews, Trainings, Product Updates, Liaised with Product Management / Sales / Partners/Support (Escalations) Secured significative up-sells / cross-sells",
                "Scope: API Management, Integration Platform as a Service, Content Services"
            ]
        },
        {
            "years": "2018",
            "title": "Senior Technical Sales Engineer",
            "company": "Viasat",
            "location": "Dublin",
            "responsibilities": [
                "Strategic pre-sales support to the sales team for complex deals (+1M€ Deals) RFI/RFP coordination + leading technical answers for AWS deployments Sales Engineering process and material improvements"
            ]
        },
        {
            "years": "2014-2018",
            "title": "Cloud Platform Pre-Sales",
            "company": "ORACLE",
            "location": "Dublin",
            "responsibilities": [
                "Present and demonstrate the Oracle Cloud portfolio (Paas/laas, 60 products) Supporting UK/IE sales team in the qualification of opportunities, analyzing customers' requirements and building cloud solution architectures",
                "Delivered Sales Enablement & Trainings (Sales Academy) Participation in demand generation programs, use case & go-to-market strategies In rotation with EMEA Product Management team, launched & lead the App Dev community Contributed to an average +1M$ revenue / year",
                "Scope: PaaS/laaS, App Dev (Cloud Native, DevOps, Docker) Integration, Content Cloud"
            ]
        },
        {
            "years": "2012-2014",
            "title": "EMEA/AP Lead Technical Account Manager & Pre-sales",
            "company": "NETVIBES (Dassault Systemes company)",
            "location": "Paris",
            "responsibilities": [
                "Set up & lead the pre-sales & TAM activities for EMEA / AP region for 3DS Netvibes Provided strategic support to the business development team (including RFPs, PoCs, customer presentations & demos, solution architecture ...) and internally to Dassault System's sales engineers in $EMEA/AP$",
                "Product Management: produced & maintained internal competitive matrix and wrote sales battle cards Closed the 1st 600k$ deal with UAE customer and 1st deal with South Korean multinational"
            ],
            "scope": "Scope: Natural Language Processing, Web Apps, APIs, Digital Marketing"
        }
    ],
    "education": [
        {
            "years": "2009-2010",
            "degree": "Master of Business Administration (MBA)",
            "school": "University of Paris 1 Pantheon Sorbonne",
            "notes": "MBA thesis on Cloud Computing obtained with Highest Honours"
        },
        {
            "years": "2001-2006",
            "degree": "IT Engineering Degree",
            "school": "Ecole Centrale d'Electronique"
        }
    ],
    "languages": {
        "English": "fluent",
        "French": "native",
        "Arabic": "native tunisian arabic",
        "Spanish": "basic spanish"
    },
    "certifications": [
        "Oracle Cloud Generative Al Professional (2025)",
        "Python Programming (O'Reilly course) (2024)",
        "Machine Learning Methods Specialized Certificate, University of California San Diego Extension (2023-2024)",
        "NVidia Certified Associate Al In the Data Center (2024)",
        "Oracle Cloud Operations Professional (2024)",
        "Algorithms (Post Graduate course), University of Leeds (2023)",
        "Oracle Autonomous Database Cloud Professional (2023)",
        "Oracle Cloud Infrastructure Architect Associate (2022)",
        "Certified Kubernetes & Cloud Native Associate (2022)",
        "Machine Learning, Stanford University via Coursera (2021)",
        "Product Management, Stanford University Continuing Studies (2018)"
    ],
    "publications": [
        "Digital, Organizational Customer Success & Experiential Solutions (Self-Published book on Amazon) (2021)",
        "Tech Blog Posts Latest: https://walidhajeri.hashnode.dev/"
    ],
    "other": "Founder"
}
"""

cv = json.loads(cv_data)

def create_map_data():
    work_locations = pd.DataFrame({
        'city': ['Paris', 'New York', 'Dublin'],
        'lat': [48.8566, 40.7128, 53.3498],
        'lon': [2.3522, -74.0060, -6.2603],
        'color': ['#FF5733'] * 3  # Orange-ish color for work
    })
    
    customer_locations = pd.DataFrame({
        'city': ['4. London', '5. Seoul', '6. Madrid', '7. Barcelona', '8. Rome', '9. Geneva',
                 '10. Amsterdam', '11. Pretoria', '12. Doha', '13. Mumbai', '14. Brussels', '15. Munich', '16. Manchester',
                 '17. Abu Dhabi', '18. Porto', '19. Rabat', '20. Oslo', '21. Helsinki', '22. Manila', '23. Fort Worth',
                 '24. Porto-Novo', '25. Abuja', '26. Praia', '27. Yamoussoukro', '28. Banjul', '29. Accra', '30. Bissau',
                 '31. Conakry', '32. Monrovia', '33. Bamako', '34. Niamey', '35. Abidjan', '36. Dakar', '37. Freetown',
                 '38. Lomé', '39. Washington, DC', '40. Marseille', '41. Lille', '42. Bordeaux', '43. Rennes'], # Added numbers
        'lat': [51.5074, 37.5665, 40.4168, 41.3851, 41.9028, 46.2022,
                52.3702, -25.7461, 25.2854, 19.0760, 50.8333, 48.1371, 53.4808,
                24.4511, 41.1496, 34.0253, 59.9139, 60.1699, 14.5995, 32.7554,
                6.4779, 9.0579, 14.9214, 6.8206, 13.4531, 5.6037, 11.8596,
                9.5167, 6.3105, 12.6500, 13.5197, 5.3524, 14.7105, 8.4605,
                6.1305, 38.8951, 43.2965, 50.6292, 44.8378, 48.1173],
        'lon': [-0.1278, 126.9780, -3.7038, 2.1734, 12.4964, 6.1490,
                4.8952, 28.1871, 51.5310, 72.8777, 4.3333, 11.5761, -2.2426,
                54.3696, -8.6291, -6.8791, 10.7522, 24.9384, 120.9772, -97.3308,
                2.6323, 7.3985, -23.5000, -5.2767, -16.5780, -0.2079, -15.5042,
                -13.7036, -10.8022, -8.0077, 2.1096, -4.0083, -17.4788, -13.1049,
                -1.3159, -77.0364, 5.3698, 3.0573, -0.5792, -1.6778],
        'color': ['#007BFF'] * 40  # Changed to 43 to match the new count
    })

    study_locations = pd.DataFrame({
        'city': ['Paris', 'Leeds', 'Tunis', 'San Diego', 'Stanford'],
        'lat': [48.8800, 53.8012, 36.8065, 32.7157, 37.4275],
        'lon': [2.3000, -1.5486, 10.1815, -117.1611, -122.1697],
        'color': ['#800080', '#800080', '#800080', '#800080', '#800080']  # Explicitly repeated color
    })
    
    other_locations = pd.DataFrame({
            'city': ['You may add other relevant cities here'],
            'lat': [0], # Replace with actual latitude
            'lon': [0], # Replace with actual longitude
            'color': ['#808080']  # Grey color for others
        })
    
    return pd.concat([work_locations, customer_locations, study_locations, other_locations], ignore_index=True)


def main():
    #st.title(f"{cv['personal']['name']} - Customer Engineer Presentation")
    st.header("Introduction")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/50/Oracle_logo.svg", width=200)

    with col2:
        st.subheader(cv["personal"]["title"])
        st.write(cv["objective"])
        st.markdown(f"**LinkedIn:** [My Profile]({cv['personal']['linkedin']})", unsafe_allow_html=True)

    st.markdown("### Why I'm a Great Fit")
    st.markdown("- Strong Experience in Customer Success")
    st.markdown("- Proven track record in technical advisory.")
    st.markdown("- Great team player, Coordinator & Customer advocate")
    st.markdown("- Used to high-stakes situations, Escalation Management")
    st.markdown("- Oracle Cloud knowledge, AI-Enthusiast => Crucial for Customer innovation & Growth")

    # --- Experience Highlights Section ---
    st.header("Experience Highlights")
    st.subheader("Relevant Professional Journey")
    for job in cv["experience"]:
        if job.get("title") != "ShopFromFrance":
            st.markdown(f"**{job['title']}**")
            st.markdown(f"*{job['company']}* ({job['years']})")
            if "responsibilities" in job:
                for responsibility in job["responsibilities"]:
                    st.markdown(f"- {responsibility}")
            st.write("---") # Separator

 # --- Skills and Responsibilities Alignment Section ---
    st.header("Deep Dive: Aligning Skills with Responsibilities")
    st.subheader("Connecting My Experience to Your Needs")

    # Define job responsibilities and corresponding examples
    responsibilities_examples = {
        "Conduct periodic Service Account Planning and Account Reviews // Establish and maintain a delivery governance model with the customer at the management and executive levels.": [
            "- At Oracle: Monthly/Quarterly Reviews + Technical Reviews + SR Reviews",
            "- At Axway: Led Quarterly Business Reviews with customers"
        ],
        "Act as a point of contact for any major incidents, responsible for managing communication and customer expectations through resolution.": [
            "- Example: Escalation Management",
        ],
        "Coordinate delivery of Oracle Services, operating as the primary delivery contact to the customer, aiding and facilitating customer communications and activities across other Oracle lines of business.": [
            "- Example: Coordinate delivery of multiple Oracle Services including Technical Workshops (e.g. Patching workshop), Technical Reviews (HC), Consumption Reviews, SR Reviews, Go Live Assurance ",
        ],
         "Identify and submit delivery leads for new opportunities and contract renewals // Work collaboratively with sales, the delivery teams and customers to identify appropriate solutions.": [
            "- Example: Uncovered multiple service delivery opportunities : Oracle Universiy, Consulting. Product needs : Full Stack Discovery need (Retail), Database Management, OS Management Hub (automotive), etc. ",
        ]
    }

    # Display responsibilities and examples
    for responsibility, examples in responsibilities_examples.items():
        st.markdown(f"**{responsibility}**")
        for example in examples:
            st.markdown(f"- {example}")

    st.header("Global Reach")
    st.subheader("Where I've Worked and Who I've Served")
    map_data = create_map_data()

    st.map(map_data,
         latitude='lat',
         longitude='lon',
         color='color')

if __name__ == "__main__":
    main()
