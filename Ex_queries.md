**Example Queries for our solar panel database**

**Schema:**\
Customer
app_id (PK) | zip_code | complete_date | contractor | cust_type | municipality | acceptance_date

Program
app_id (FK) | zip_code | complete_date | contractor | cust_type | municipality | acceptance_date
Cost

app_id (FK) | third_ownership | Interconnection
Power

app_id (FK) | third_ownership | Interconnection

**Queries:**\
**1. Select all customers who have completed their solar panel installations:**
<pre>
  SELECT * FROM Customer WHERE complete_date IS NOT NULL;
</pre>
This query will return all rows from the "Customer" table where the "complete_date" column is not null, meaning the customer has completed their solar panel installation.


**2. Calculate the total number of customers who have third-party ownership of their solar panels:**
<pre>
  SELECT COUNT(*) FROM Cost WHERE third_ownership = TRUE
</pre>
This query will return the total number of rows from the "Cost" table where the "third_ownership" column is true, indicating that the customer has third-party ownership of their solar panels.


**3. Calculate the total cost of solar panel installations for customers who have accepted the program, grouped by municipality:**
<pre>

  SELECT municipality, SUM(CASE WHEN third_ownership THEN 0 ELSE 1 END * interconnection_cost) AS total_cost
  FROM (
    SELECT p.municipality, c.third_ownership, c.interconnection AS interconnection_cost
    FROM Program p
    JOIN Cost c ON p.app_id = c.app_id
    WHERE p.acceptance_date IS NOT NULL
  ) subquery
  GROUP BY municipality;
</pre>

This query retrieves the municipality and cost information for customers who have accepted the program, but calculates the cost differently based on whether the customer has third-party ownership of their solar panels. It does this by joining the "Program" and "Cost" tables on "app_id", and then calculating the cost as either the "interconnection" cost (if the customer owns their solar panels) or zero (if a third party owns the panels). It then groups the results by municipality and calculates the total cost for each group.


**4. Find the top 5 municipalities by number of solar panel installations completed in the past year:**
<pre>
  SELECT c.municipality, COUNT(*) AS num_installations
  FROM Customer c
  WHERE c.complete_date >= NOW() - INTERVAL '1 year'
  GROUP BY c.municipality
  ORDER BY num_installations DESC
  LIMIT 5;
</pre>


**5. This query retrieves the municipality and count information for all solar panel installations completed in the past year, and then orders the results by the number of installations in descending order. It returns only the top 5 municipalities by adding a "LIMIT" clause to the end of the query.**

Calculate the average power generation for customers who have accepted the program, but exclude customers who have a third-party owner and have not connected to the power grid:
<pre>
  SELECT AVG(p.power_generation) AS avg_power
  FROM Program pr
  JOIN Power p ON pr.app_id = p.app_id
  JOIN Cost c ON pr.app_id = c.app_id
  WHERE pr.acceptance_date IS NOT NULL
  AND (c.third_ownership = FALSE OR (c.third_ownership = TRUE AND p.interconnection = TRUE));
</pre>

This query retrieves the average power generation for customers who have accepted the program, but excludes customers who have third-party ownership of their solar panels and have not connected to the power grid. It does this by joining the "Program", "Power", and "Cost" tables on "app_id", and then filtering the results to only include rows where the customer has accepted the program and either does not have third-party ownership or has connected to the power grid.

