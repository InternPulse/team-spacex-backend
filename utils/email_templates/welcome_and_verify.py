WELCOME = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Verification</title>
    <style>
        @import url('https://fonts.googleapis.com/css?family=Ubuntu:400,700&display=swap');
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: Ubuntu, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            color: #666666;


        }}
        
        h1 {{
            color: #333333;
            margin-top: 0;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }}
        @media (prefers-color-scheme: dark) {{
            body {{
                background-color: #333333;
                color: whitesmoke;
            }}
            .container {{
                background-color: #666;
                color: whitesmoke;
            }}
            h1 {{
                color: white;
            }}
        }}
        p {{
            margin-bottom: 20px;
        }}
        ul {{
            list-style-type:circle;
            margin-top: 0;
            padding-left: 20px;
            margin-bottom: 20px;
        }}
        li {{
            margin-top: 10px;
        }}
        .button {{
            display: inline-block;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            width: 150px;
            height: 40px;
            padding: 10px 20px;
            margin: 10px 0 25px;
            border-radius: 5px;
            box-shadow: 2px 2px 2px #333333;
        }}
        a {{
            text-decoration: none;
        }}
        a:active {{
            text-decoration: none;
        }}

        .button:active {{
            background-color: #0056b3;
            font-weight: 800;
        }}
        .socials a img {{
            width: 30px;
            height: 30px;
            margin-right: 10px;
        }}
    </style>
</head>

<body>
    <div class="container">
        <h1>Welcome</h1>
        <p>Dear {user},</p>
        <p> You're most highly welcome to InternPilot, An application designed to ease your comfort and prepare quick
            and ready invoices
            for your users, as well as keep records of these invoices allowing you to easily track oyour sales and
            records.</p>
        <p>With InvoicePilot, You can</p>
        <ul>
            <li>Prepare automated and customized invoices</li>
            <li>Track customer pattern based on purchases and identify customer's preferences</li>
            <li>Send invoices to customers email allowing them to have their own copy incase they lose it</li>
            <li>And if you can't find the email, simply recreate the invoice from the records</li>
        </ul>
        <p>But before all that happens, you need to verify your account to gain access to all of these perks. Unverified accounts
            will be deleted after 14 days. To avoid being in that category, click the button below to verify your account.
        </p>
        <a href="{link}"><button class="button">Verify Email</button></a>
        <p>If you did not sign up for an account with Invoicepilot, you can safely ignore this email.</p>
        <p>Best regards,<br>Invoicepilot Team</p>
        <div class="socials">
            <a href="https://twitter.com/InternPulseHQ" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/twitter.png" alt="Twitter"></a>
            <a href="https://www.instagram.com/InternPulse/" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="Instagram"></a>
            <a href="https://facebook.com/internpulsehq/" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/facebook-new.png" alt="Facebook"></a>
            <a href="https://www.linkedin.com/company/internpulse" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn"></a>
            <a href="mailto:internpulsehq@gmail.com"><img src="https://img.icons8.com/fluent/48/000000/gmail.png" alt="Gmail"></a>
            <a href="https://internpulse.com"><img src="https://img.icons8.com/ios/50/000000/internet--v1.png" alt="Web"></a>
        </div>
    </div>
</body>
</html>"""

W_TEXT = """Welcome
Dear {user},
You're most highly welcome to InternPilot, An application designed to ease your comfort and prepare quick
and ready invoices
for your users, as well as keep records of these invoices allowing you to easily track oyour sales and
records.
With InvoicePilot, You can
    Prepare automated and customized invoices
    Track customer pattern based on purchases and identify customer's preferences
    Send invoices to customers email allowing them to have their own copy incase they lose it
    And if you can't find the email, simply recreate the invoice from the records
But before all that happens, you need to verify your account to gain access to all of these perks. Unverified accounts
will be deleted after 14 days. To avoid being in that category, click the link below to verify your account.
{link}
If you did not sign up for an account with Invoicepilot, you can safely ignore this email.
Best regards, Invoicepilot Team
"""