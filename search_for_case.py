
# Greet function: (this might appear elsewhere in the code already, and just needs to be modified)
## initialize a SCOPE bool, criminal_type bool, and 'Delhi' bool.
## greet user and ask what they need help with
## if request is related to case information, set SCOPE bool to true. otherwise, set SCOPE bool to false
## confirm with user that case is a criminal case (criminal_type = true) and located in delhi (state = true). if either are not true, switch scope to false
while not scope:
     #say "i'm sorry, this prototype can only help you find criminal cases in Delhi. Is there a criminal case in Delhi I can help you with?" and if user says yes, switch flags to true. otherwise, exit search program


##if scope == true, begin search process:

# main case search info collection function: collect_case_query_info(). this program collects info necessary to lookup a case
## initialize a new "case query information" structure which can store the following:
## 0. Has_CNR bool (initialize to none)
## 1. CNR Number (16-character string)
## 2. Delhi (true by default)
## 3. District (not sure what data type is best, can be one of the following options: central, east, new delhi, north, north east, north west, shahdara, south, south east, south west, west)
## 4. Court Complex (not sure what data type is best, but here are the options: 
## 5. Year (array of ints)
## 6. Petitioner Name (string)
## 7. Respondent Name (string)
## 8. Filing Number (int)
## 9. Advocate Name (string)
## 10. Police station (one value out of list of police station strings probably)
## 11. FIR Number (int)
## 12. Pending (bool, initialized as NONE, if case has been closed then it's false, if case is still at trial then it's true) 
## 13. Criminal_type (bool) = true by default

## once new case query has been created, store new instance in postgresql database

# Helper function: get_CNR()
## ask for CNR number if they did not provide it yet. be prepared to have a conversation about this.
# if the user gives the CNR number, create a helper function to check if it is in the format: ^[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{6}$
## if at any point during the lookup conversation the user finds the CNR, call get_cnr()

## Ask what district in Delhi it happened. Use the logic below to determine the complex based on the user's response.
if District == Central:
    if high_profile == true:  ##This complex only handles high-profile, CBI cases. Ask the user if this sounds like their case. If they don't know, assume false.
        complex = Rouse Avenue Court Complex
    else complex = Tis Hazari Court Complex
if District == East or North East or Shahdara:
    complex = Karkardooma Court Complex
if District == New Delhi:
    complex = Patiala House Court Complex
if District == North or North West:
    complex = Rohini Court Complex
if District == South or South East:
    complex = Saket Court Complex
if District == South West:
    complex = Dwarka Court Complex
if District == West:
    complex = Tis Hazari Court Complex

if complex = Tis Hazari Court Complex:
        if criminal_case_type == true:  ## must ask user to see if their case is criminal or civil. if it is criminal, set this to true
            Establishment = Chief Metropolitan Magistrate, West, THC

# ask what year the case happened in. Tell them if they are unsure, they can give you a range. Store each individual year as a different entry in the year array