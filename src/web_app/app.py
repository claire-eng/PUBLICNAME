#! /usr/bin/python3
import psycopg2
from config import config
from flask import Flask, render_template, request
import random
import string

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')

        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows

# app.py
app = Flask(__name__, static_folder='static')

# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

@app.route('/query')
def query():
    return render_template('query.html')

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))


# handle query POST and serve result web page
@app.route('/query-handler', methods=['POST'])
def query_handler():
    try:
        temp = request.form["test"]
        temp2 = int(request.form["test2"])
        temp3 = request.form["test3"]
        temp4 = request.form["test4"]
        temp5 = request.form["test5"]
        temp6 = int(request.form["test6"])
        
        if (temp6 == 1):
            table1heads = ['Municipality', 'Average KW Usage Per Municipality']
            table1rows = connect(temp5)
            table2heads = ['Municipality', 'Most Prominent Electric Utility', 'Count']
            table2rows = connect(temp3)
            table3heads = ['Municipality', 'Most Prominent Customer Type', 'Count']
            table3rows = connect(temp4)
            table4heads = ['KW Usage', 'Municipality', 'Application ID', 'Zip Code', 'Customer Type', 'Contractor']
            table4rows = connect(temp)
            return render_template(
                'my-result.html', 
                table1heads = table1heads, table1rows = table1rows,
                table2heads = table2heads, table2rows = table2rows,
                table3heads = table3heads, table3rows = table3rows,
                table4heads = table4heads, table4rows = table4rows,
            )
                
        if (temp6 == 2):
            table1heads = ['Electric Utility Company', 'Average KW Usage Per Electric Utility Company']
            table1rows = connect(temp5)
            table2heads = ['Electric Utility Company', 'Most Prominent Customer Type', 'Count']
            table2rows = connect(temp3)
            table3heads = ['Electric Utility Company', 'Municipality With Highest Electric Utility Count', 'Count']
            table3rows = connect(temp4)
            table4heads = ['KW Usage', 'Electric Utility Company', 'Municipality', 'Application ID', 'Zip Code', 'Customer Type', 'Contractor']
            table4rows = connect(temp)
            return render_template(
                'my-result.html', 
                table1heads = table1heads, table1rows = table1rows,
                table2heads = table2heads, table2rows = table2rows,
                table3heads = table3heads, table3rows = table3rows,
                table4heads = table4heads, table4rows = table4rows,
            )
        
        if (temp6 == 3):
            table1heads = ['Customer Type', 'Average KW Usage Per Customer Type']
            table1rows = connect(temp5)
            table2heads = ['Customer Type', 'Municipality that Customer Type is most Prominent in', 'Count']
            table2rows = connect(temp3)
            table3heads = ['Customer Type', 'Most Popular Electric Utility With Customer Type', 'Count']
            table3rows = connect(temp4)
            table4heads = ['KW Usage', 'Customer Type', 'Municipality', 'Application ID', 'Zip Code', 'Contractor']
            table4rows = connect(temp)
            return render_template(
                'my-result.html', 
                table1heads = table1heads, table1rows = table1rows,
                table2heads = table2heads, table2rows = table2rows,
                table3heads = table3heads, table3rows = table3rows,
                table4heads = table4heads, table4rows = table4rows,
            )
            
        
        return render_template(
                    'my-result.html', 
                    table1heads = table1heads, table1rows = table1rows,
                    table2heads = table2heads, table2rows = table2rows,
                    table3heads = table3heads, table3rows = table3rows,
                    table4heads = table4heads, table4rows = table4rows,
        )
    except:
        return render_template('error.html'), 500

if __name__ == '__main__':
    app.run(debug = True)
