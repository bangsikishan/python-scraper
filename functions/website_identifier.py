import emoji

from scripts import get_procurement_bids

def identify_website(url):
    if "bids.aspx" in url or "Bids.aspx" in url:
        print(emoji.emojize("[+] :check_mark:  IDENTIFIED AS BIDS.ASPX WEBSITE!"))
    elif "procurement.opengov" in url:
        print(emoji.emojize("[+] :check_mark:  IDENTIFIED AS PROCUREMENT WEBSITE!"))
        get_procurement_bids(url)
    else:
        print(emoji.emojize("[-] :cross_mark: COULD NOT IDENTIFY THE WEBSITE! CONTINUING..."))
