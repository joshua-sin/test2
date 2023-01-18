from BlogApp import app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True) 
    


'''
Change front-end templates;
    - notification widget (refer to: https://tailwindcomponents.com/component/notification-3)
'''

'''
- general.py function subs_success
'''

'''SCR
@general.route("/scr", methods=['GET','POST'])    #scr --> show contact results
def scr():
    if os.path.exists("contact_data.json"):    
        with open("contact_data.json") as datafile:
            saveddata = json.load(datafile)
    else:
        saveddata = {}

    if request.method == "POST":
        saveddata[request.form['email']] = request.form

    with open("BlogApp/contact_data.json", "w") as datafile: 
        json.dump(saveddata, datafile)

    if current_user.is_authenticated:
        return render_template('general/scr.html', form=saveddata)    
    else:
        return redirect(url_for('general.about_us'))
'''

'''
1. Home

2. About Us (dropdown) → 
our people (introduce house exco and house teachers), 
our mission (describe the moor house moto, mission, crest and cheer), 
our history (timeline and key milestones)
your role (motivate moorians to participate more and earn house points)

3. Updates

4. Blogs

5. Merch (design voting)

6. Contact Us
'''

'''
Checkout page if we are implementing a cart system: https://larainfo.com/blogs/tailwind-css-simple-ecommerce-checkout-page-ui-example
Shopping cart: https://codepen.io/abdelrhman/pen/BaNPVJO or https://tailwindui.com/components/ecommerce/page-examples/shopping-cart-pages
'''

'''
Ideas for shopping cart: 
1. Make a table called cart and have user.id and product.id as foreign keys
2. use flask sessions to store the cart items
'''

'''
Questions to ask Mrs Neo;
1. How to implement a shopping cart system?
2. Payment by credit card
3. Security stuff that needs to be done after the website is created
4. How and where to host website after development?
'''