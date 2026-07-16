class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueset=set()
        for email in emails:
            local,domain=email.split("@")
            # remove all part after +
            local=local.split("+")[0]
            # remove the dots
            local=local.replace(".","")
            new_mail=local+"@"+domain
            uniqueset.add(new_mail)
        return len(uniqueset)