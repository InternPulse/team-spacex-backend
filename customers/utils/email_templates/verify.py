VERIFY_ACCOUNT = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verify your email</title>
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
            width: 80%;
            margin: auto;
            display: flex;
            flex-flow: column;
            justify-content: flex-start;
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
            text-align: center;
            color: #ffffff;
            text-decoration: none;
            width: 200px;
            height: 40px;
            align-self: center;
            padding: 10px 20px;
            margin: 10px auto 25px;
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
        <h1>Verify your account</h1>
        <p>Hi {user},</p>
        <p>You haven't verified your account? Please verify your account in order to gain full access to all of
            InvoicePilot's amazing features. Remember all unverified accounts will be deleted 14 days after creation
            Tap the button below to verify your email.
        </p>
        <a href="{link}"><button class="button">Verify Your Email</button></a>
        <ul>
            If you:
            <li>Have already verified your email</li>
            <li>Didn't request for a verification link or</li>
            <li>Didn't ask for this email</li>
            you can safely ignore this email.
        </ul>
        <p>Best regards,<br>Invoicepilot Team</p>
        <div class="socials">
            <a href="https://twitter.com/InternPulse" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/twitter.png" alt="Twitter"></a>
            <a href="https://www.instagram.com/internpulse/" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="Instagram"></a>
            <a href="https://www.facebook.com/InternPulse" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/facebook-new.png" alt="Facebook"></a>
            <a href="https://www.linkedin.com/company/internpulse" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn"></a>
            <a href="mailto:internpulse@gmail.com"><img src="https://img.icons8.com/fluent/48/000000/gmail.png" alt="Gmail"></a>        </div>
    </div>
</body>
</html>"""
VA_TEXT = """Verify your account
Hi {user},
You haven't verified your account? Please verify your account in order to gain full access to all of \
InvoicePilot's amazing features. Remember all unverified accounts will be deleted 14 days after creation.\
Click on the link below to verify your email.
{link}
If you:
    Have already verified your email
    Didn't request for a verification link or
    Didn't ask for this email
    you can safely ignore this email.
Best regards, Invoicepilot Team
"""