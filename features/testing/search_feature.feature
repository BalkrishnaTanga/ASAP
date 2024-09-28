Feature:  Search Functionality

  Scenario Outline: Verify employee + button is visible in Search for new SSN
    Given : Navigate to Home page
    When Enter the new employee numbers <ssn>
    Then employee information popup should open
    Examples:;
      | ssn         |
      | 323-22-4444 |


  Scenario Outline: Verify employee button should be disabled for exiting ssn number
    Given : Navigate to Home page
    When enter already existing employee <ssn>
    Then verify the employee button is <disabled>
    Examples:;
      | ssn         | disabled |
      | 11-111-1111 | true     |
      | 12-22-22222  | true    |

  Scenario Outline: Verify new employee + button is visible in search with new Last 4 Digit of SSN and Last Name
    Given : Navigate to Home page
    Given last <option> digit option is selected from dropdown
    And Enter last 4 digit ssn <last4digits> and last name <lastname>
    When user click on add employee button
    Then employee information popup should open
    Examples:
      | option                            |last4digits|lastname |
      | Last 4 digits of SSN and Last Name|   4555    |   themes|

  Scenario Outline: Verify new employee + button be disabled  in search with new Last 4 Digit of SSN and Last Name
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter existing last 4 digit ssn <last4digits> and last name <lastname>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
      | option | last4digits | lastname | disabled |
      | Last 4 digits of SSN and Last Name|   1111    |   MaGuest| true |

  Scenario Outline: Verify new employee + button is visible in search with new LastName,FirstName
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the names  <lastname_firstName>
    When user click on add employee button
    Then employee information popup should open
    Examples:
      | option  | lastname_firstName |
      | LastName,FirstName   |   yadav1,bala1     |

  Scenario Outline: Verify new   employee + button is disable mode in search with existing LastName,FirstName
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the names  <lastname_firstName>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
        | option  | lastname_firstName | disabled |
        | LastName,FirstName   |   yadav,bala     | true|

  Scenario Outline: Verify new employee + button is visible in search with new Email
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the email  <email>
    When user click on add employee button
    Then employee information popup should open
    Examples:
          | option  | email |
          | Email |   bala+1@uyopmail.com    |

  Scenario Outline:  Verify employee + button is disable mode in search with existing email
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the email  <email>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
            | option  | email | disabled |
            | Email  |   5EDCEA67-C3C3@osca.com    | true|

  Scenario Outline:  Verify new employee + button is visible in search with new lastname
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the lastname <lastName>
    When user click on add employee button
    Then employee information popup should open
    Examples:
              | option  | lastName |
              | Last Name |   MaGuest1  |

  Scenario Outline: Verify  new employee + button is disable mode in search with  existing lastname
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the lastname <lastName>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
      | option  | lastName | disabled |
      | Last Name |   MaGuest    | true |

  Scenario Outline: Verify new employee +button is visible in search with new firstname
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the firstname  <firstname>
    When user click on add employee button
    Then employee information popup should open
    Examples:
                | option  | firstname |
                | First Name |   MaSamplem    |

  @regression
  Scenario Outline: Verify  new employee + button is disable mode in search with  existing firstname
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the firstname  <firstname>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
       | option  | firstname | disabled |
       | First Name |   MaSample    | true |


  Scenario Outline: Verify new employee +button is visible in search with new Passport#
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the passportno  <passportno>
    When user click on add employee button
    Then employee information popup should open
    Examples:
                | option  | passportno |
                | Passport # |   F22324232   |

  Scenario Outline:  Verify  new employee + button is disable mode in search with Existing Passport#
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the passportno  <passportno>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
    | option  | passportno | disabled |
    | Passport # |   F8954440   | true |

  Scenario Outline: Verify new employee +button is visible in search with new Driverlicense
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the driverlicense   <driverlicense>
    When user click on add employee button
    Then employee information popup should open
    Examples:
              | option  | driverlicense |
              | Driver License # |   4242141   |

  Scenario Outline: Verify new employee +button is disable mode in search with existing Driverlicense
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the driverlicense   <driverlicense>
    When user click on add employee button
    Then  verify the employee button is <disabled>
    Examples:
      | option  | driverlicense | disabled |
      | Driver License # |   A1234567  | true |

  Scenario Outline: Verify new employee +button is visible in search with new PersonId
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the personId   <personId>
    When user click on add employee button
    Then employee information popup should open
    Examples:
              | option  | personId |
              | PersonId |   24241221   |

  Scenario Outline: Verify new employee +button is disable in search with existing PersonId
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    And Enter the personId   <personId>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
      | option  | personId | disabled |
      | PersonId |   232323   | true|

  Scenario Outline: Verify new employee +button is visible in search with new Employee/RefId
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    When Enter the <company_name>
    And User the employee_ref_id on search employee page <employee_ref_id>
    When user click on add employee button
    Then employee information popup should open
    Examples:
              | option  | employee_ref_id |company_name |
              | Employee/Ref Id |   3121312   |  AA010110       |

  Scenario Outline: Verify new employee + button is disable id search with existing  Employee/RefId
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    When Enter the <company_name>
    And User the employee_ref_id on search employee page <employee_ref_id>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
      | option  | employee_ref_id |company_name | disabled |
      | Employee/Ref Id |   D232434   |  C-MM000012       | true |

  Scenario Outline:  Verify new employee+ button is visible in search with new ApplicationID
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    When Enter the <company_name>
    And User the application id on search epage <application_id>
    When user click on add employee button
    Then employee information popup should open
    Examples:
              | option  | application_id |company_name |
              | Application Id |   852122   |  AA010110       |

  Scenario Outline:  Verify new employee+ button is disable in search with existing ApplicationID
    Given : Navigate to Home page
    And last <option> digit option is selected from dropdown
    When Enter the <company_name>
    And User the application id on search epage <application_id>
    When user click on add employee button
    Then verify the employee button is <disabled>
    Examples:
      | option  | application_id |company_name | disabled |
      | Application Id |   A23423   |  C-MM000012       | true |

  Scenario: Demo failed test cases
    Given : Navigate to Home page
    Then Fail the test case