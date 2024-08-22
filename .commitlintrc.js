module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "body-max-line-length": [0, "always", 0], // Disable line length checking for the body
    "body-max-length": [0, "always", Infinity], // Disable total body length checking
    "header-max-length": [0, "always", 0], // Disable header length checking
    "footer-max-line-length": [0, "always", 0], // Disable line length checking for the footer
    "footer-max-length": [0, "always", Infinity], // Disable total footer length checking
  },
};
