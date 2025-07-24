// Custom commands for Cypress
cy.commands('login', (username, password) => {
  cy.visit('/login');
  cy.get('#username').type(username);
  cy.get('#password').type(password);
  cy.get('button[type="submit"]').click();
});

cy.commands('submitPermitApplication', (applicationData) => {
  cy.visit('/apply');
  //Fill out the form based on applicationData
  cy.get('#permitType').select(applicationData.permitType);
  // ... other form fields ...
  cy.get('button[type="submit"]').click();
});