import re
import json

# Load CV data (replace with actual data loading if needed)
cv_data = """
{
"personal": {
    "name": "WALID HAJERI",
    "title": "Cloud/Al Customer Engineer",
    "location": "Paris Region, France",
    "linkedin": "http://www.linkedin.com/in/walidhajeri"
  },
  "objective": "Accomplished Customer Success Engineer with a strong background in Cloud and App Dev, now Leveraging expertise in Al. Recently certified in Machine Learning Methods from UC San Diego Extension, with hands-on experience in Generative Al and Large Language Models (LLMs). A thought leader and strong communicator with a passion for innovative tech products, offering international experience (US, Ireland) across both enterprise and startup environments. Seeking a challenging role in a dynamic, international setting.",
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
      "company": "axway",
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
      "company": "Viasatw",
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
      "company": "BS NETVIBES (Dassault Systemes company)",
      "location": "Paris",
      "responsibilities": [
        "Set up & lead the pre-sales & TAM activities for EMEA / AP region for 3DS Netvibes Provided strategic support to the business development team (including RFPs, PoCs, customer presentations & demos, solution architecture ...) and internally to Dassault System's sales engineers in $EMEA/AP$",
        "Product Management: produced & maintained internal competitive matrix and wrote sales battle cards Closed the 1st 600k$ deal with UAE customer and 1st deal with South Korean multinational"
      ],
      "scope": "Scope: Natural Language Processing, Web Apps, APIs, Digital Marketing"
    },
    {
      "years": "2011-2012",
      "company": "ShopFromFrance",
      "location": "Paris",
      "responsibilities": "In charge of all operations, including international remote team management, website development, digital marketing activities Served customers all over the world including Middle East, Australia, Europe, USA"
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

job_description = """
About the job
As a Sales Engineer, you will be the technical bridge between our sales team and our prospects. You will use your technical expertise to understand customer needs, demonstrate our product's value, and build trust throughout the sales process.

Responsibilities

    Provide technical expertise and guidance to sales team and prospects.
    Conduct product demonstrations and presentations.
    Develop and deliver Proofs of Concept (POCs).
    Respond to technical inquiries and RFPs.
    Build strong relationships with key technical stakeholders.
    Stay up-to-date on industry trends and technologies.

Qualifications

    Bachelor's degree in a technical field (e.g., Computer Science, Engineering).
    3+ years of experience as a Sales Engineer or similar role.
    Strong technical skills in [relevant technologies - to be specified based on the company].
    Excellent communication and presentation skills.
    Ability to understand customer needs and translate them into technical solutions.
    Proven track record of success in a sales environment.
"""

cv = json.loads(cv_data)

# Extract relevant information from the job description
job_responsibilities = [item.strip() for item in re.split(r'\n\s*', job_description.split("Responsibilities")[1].split("Qualifications")[0]) if item.strip()]
job_qualifications = [item.strip() for item in re.split(r'\n\s*', job_description.split("Qualifications")[1]) if item.strip()]

#print(f"Responsibilities: {job_responsibilities}")
#print(f"Qualifications: {job_qualifications}")

# Streamlit App Outline
streamlit_outline = {
    "app_title": "Walid Hajeri - Sales Engineer Presentation",
    "sections": [
        {
            "title": "Introduction",
            "content": [
                {"type": "markdown", "text": f"# {cv['personal']['name']}"},
                {"type": "markdown", "text": f"## {cv['personal']['title']}"},
                {"type": "markdown", "text": f"**Contact:** {cv['personal']['linkedin']}"},
                {"type": "markdown", "text": f"{cv['objective']}"},
                {"type": "image", "url": "your_company_logo.png", "alt": "Company Logo", "width": 200}, # Replace with actual company logo
                {"type": "markdown", "text": "### Why Walid for this role?"},
                {"type": "markdown", "text": "- Strong alignment with Sales Engineer responsibilities."},
                {"type": "markdown", "text": "- Proven track record in customer success and technical advisory."},
                {"type": "markdown", "text": "- Expertise in cloud technologies and AI, crucial for innovation."},
            ]
        },
        {
            "title": "Experience Highlights",
            "content": [
                {"type": "markdown", "text": "## Relevant Experience"},
                {"type": "experience_slider", "experience": [exp for exp in cv['experience'] if exp.get('title') not in ["ShopFromFrance"]]}, # Filter out irrelevant experience
            ]
        },
        {
          "title": "Deep Dive: Aligning Skills with Responsibilities",
          "content": [
              {"type": "markdown", "text": "## Skills & Responsibilities Matching"},
              {"type": "markdown", "text": "Here's how my experience directly addresses the key responsibilities of the Sales Engineer role:"},
              {"type": "responsibilities_grid", "responsibilities": job_responsibilities, "cv_data": cv_data}
          ]
        },
        {
            "title": "Technical Prowess",
            "content": [
                {"type": "markdown", "text": "## Technical Skills & Certifications"},
                {"type": "markdown", "text": "A snapshot of my technical capabilities:"},
                {"type": "certifications_carousel", "certifications": cv['certifications']},
                {"type": "markdown", "text": "And much more! (See LinkedIn for details)"}
            ]
        },
        {
            "title": "A Bit of Fun",
            "content": [
                {"type": "markdown", "text": "## Beyond the Resume"},
                {"type": "markdown", "text": "A glimpse into my passion for technology and communication:"},
                {"type": "markdown", "text": f"* Author: '{cv['publications'][0]}'"},
                {"type": "markdown", "text": f"* Tech Blogger:  [Walid's Blog]({cv['publications'][1].split('Latest: ')[1]})"},
            ]
        },
        {
            "title": "Let's Connect",
            "content": [
                {"type": "markdown", "text": "## Ready to Drive Success Together"},
                {"type": "markdown", "text": "I'm excited about the opportunity to bring my experience and passion to your team."},
                {"type": "markdown", "text": "**Linkedin:** {cv['personal']['linkedin']}"},
                {"type": "markdown", "text": "Thank you for your time!"}
            ]
        }
    ]
}

print(json.dumps(streamlit_outline, indent=4))
#print(cv_data)
#print(job_description)
