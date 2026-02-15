# Dependabot Security Updates Demo

This repository demonstrates automated dependency security updates using GitHub Dependabot.

## Configuration

- **Package Ecosystem**: Python (pip)
- **Update Schedule**: Weekly
- **Commit Prefix**: deps

## Dependencies

This project includes:
- FastAPI - Modern web framework
- Requests - HTTP library
- Pandas - Data analysis library

## Student Email

25ds1000107@ds.study.iitm.ac.in

## How Dependabot Works

Dependabot automatically:
1. Monitors dependencies in `requirements.txt`
2. Checks for security vulnerabilities
3. Creates pull requests for updates
4. Keeps dependencies secure without manual monitoring

## Case Study Relevance

Similar to the production API scenario, this configuration ensures that any CVE disclosure in our dependencies (requests, fastapi, pandas) will trigger automatic PRs within 24 hours, preventing the 6-month vulnerable state described in the case study.
