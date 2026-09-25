CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY 
    
      SELECT DISTINCT e1.salary AS getHighestSalary FROM Employee e1
      where N-1 = (SELECT  COUNT(DISTINCT e2.salary) FROM EMployee e2
                    WHERE e2.salary > e1.salary
    );
END;
$$ LANGUAGE plpgsql;