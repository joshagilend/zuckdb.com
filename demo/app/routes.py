from flask import Blueprint, render_template, request, current_app

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html', title="RetroScope")

@main.route('/search', methods=['GET', 'POST'])
def search():
    results = None
    if request.method == 'POST':
        query = request.form['query']
        supabase = current_app.config['SUPABASE_CLIENT']
        
        # Example query to Supabase (this will depend on your database schema)
        response = supabase.from_('your_table').select('*').ilike('your_column', f'%{query}%').execute()
        results = response.data
        
    return render_template('search.html', title="Search Trends", results=results)
@main.route('/trends')

def trends():
    supabase = current_app.config['SUPABASE_CLIENT']
    
    # Example query to Supabase (this will depend on your database schema)
    response = supabase.from_('your_trends_table').select('*').execute()
    trends = response.data
    
    return render_template('trends.html', title="Trends Analysis", trends=trends)

@main.route('/clues')
def clues():
    supabase = current_app.config['SUPABASE_CLIENT']
    
    # Example query to Supabase (this will depend on your database schema)
    response = supabase.from_('your_clues_table').select('*').execute()
    clues = response.data
    
    return render_template('clues.html', title="Clues", clues=clues)


@main.route('/about')
def about():
    return render_template('about.html', title="About RetroScope")
