import urllib as u
import time as t


#this is a change
url = "http://s2.ol-digital.com/paybill/machakos.php?id=467224212&orig=MPESA&dest=254717067932&tstamp=2016-06-05+06%3A38%3A52&text=KF56WQ7ZGU+Confirmed.+on+5%2F6%2F16+at+6%3A38+AM+Ksh600.00+received+from+CATHERINE+KIOKO+254713331625.++Account+Number+0713331625+New+Utility+balance+is+Ksh2%2C6&customer_id=8071&user=default&pass=default&routemethod_id=2&routemethod_name=HTTP&mpesa_code=KF56WQ7ZGU&mpesa_acc=0713331625&mpesa_msisdn=254713331625&mpesa_trx_date=5%2F6%2F16&mpesa_trx_time=6%3A38+AM&mpesa_amt=600.0&mpesa_sender=CATHERINE+KIOKO&business_number=656500"

average = 0
cumulative = 0
start = t.time()

for i in range(100):
    n = t.time()
    fd = u.urlopen(url)
    print "Conducting test no.: %s"%i
    print fd.read()
    tm = t.time()-n
    print "Response time %s"%tm
    average = (tm+(average*float(i)))/(i+1)
    print "Average response time so far: %s"%average
    print "Transactions per seconds %s"%((t.time()-float(start))/int(i+1))
