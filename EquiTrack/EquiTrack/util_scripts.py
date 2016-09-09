from __future__ import print_function
from django.db import connection
from django.db.models import Count, Q
import time
from datetime import datetime, timedelta
from users.models import Country
from reports.models import ResultType, Result, CountryProgramme, Indicator





def printtf(*args):
    print([arg for arg in args])
    f = open('mylogs.txt','a')
    print([arg for arg in args], file=f)
    f.close()

def set_country(name):
    connection.set_tenant(Country.objects.get(name=name))


def fix_duplicate_indicators(country_name):
    if not country_name:
        printtf("country name required /n")
    set_country(country_name)

    fattrs = ["ramindicator_set"]

    def fix_indicator_code():
        printtf('cleaning codes of indicators for country ', country_name)
        indicators = Indicator.objects.filter(code__exact='').all()
        for ind in indicators:
            ind.code = None
            ind.save()
        time.sleep(3)
    fix_indicator_code()

    def relates_to_anything(cobj):
        for a in fattrs:
            if getattr(cobj, a).count():
                printtf(cobj.id, cobj, "relates to ", a)
                return True
        return False
    def update_relationships(dpres, keep):
        for a in fattrs:
            objs = getattr(dpres, a).all()
            if len(objs):
                for obj in objs:
                    obj.indicator = keep
                    obj.save()
                    printtf("saved obj.id={} obj {} with keepid{} keep {}".format(obj.id, obj, keep.id, keep))

    def _run_clean(dupes):
        printtf(len(dupes), dupes)
        for dup in dupes:
            dupresults = Indicator.objects.filter(code=dup['code'], result=dup['result']).all()
            delq = []
            keep = None
            for dpres in dupresults:
                if not keep:
                    keep = dpres
                    continue
                else:
                    error = False
                    if relates_to_anything(dpres):
                        try:
                            update_relationships(dpres, keep)
                        except Exception as exp:
                            printtf('Cannot remove Object {}, id={}'.format(dpres, dpres.id))
                            error = True
                    if error:
                        printtf("ERROR OCCURED ON RECORD", dpres.id, dpres)
                        continue
                    delq.append(dpres)
            if not len(delq):
                printtf("Nothing is getting removed for {}".format(dupes))
            else:
                # delete everyting in the queue
                [i.delete() for i in delq]
                printtf("deleting: ", delq)

    dupes = Indicator.objects.values('code', 'result').order_by('code', 'result').annotate(Count('pk')).filter(pk__count__gt=1).all()
    _run_clean(dupes)

def fix_duplicate_results(country_name):

    if not country_name:
        printtf("country name required /n")
    set_country(country_name)
    # foreign attributes
    fattrs = ["governmentinterventionresult_set",
            "indicator_set",
            "ramindicator_set",
            "resultchain_set",
            "tripfunds_set"]
    fattrs_mapping = {
        "governmentinterventionresult_set" : "result",
        "indicator_set" : "result",
        "ramindicator_set": "result",
        "resultchain_set": "result",
        "tripfunds_set": "wbs"
    }
    def fix_string_wbs():
        results = Result.objects.filter(wbs__exact='').all()
        for res in results:
            res.wbs = None
            res.save()
    fix_string_wbs()

    def reparent_children(current_object, new_parent):
        for child in current_object.get_children():
            child.parent = new_parent
            printtf( "reparenting child", child.id, child, new_parent.id, new_parent)
            child.save()
    def relates_to_anything(cobj):
        for a in fattrs:
            if getattr(cobj, a).count():
                printtf(cobj.id, cobj, "relates to ", a)
                return True
        return False
    def update_relationships(dpres, keep):
        for a in fattrs:
            objs = getattr(dpres, a).all()
            if len(objs):
                for obj in objs:
                    if a == "tripfunds_set":
                        obj.wbs = keep
                    else:
                        obj.result = keep
                    obj.save()
                    printtf("saved obj.id={} obj {} with keepid{} keep {}".format(obj.id, obj, keep.id, keep))
    def _run_clean(prop, dupes):
        printtf(len(dupes), dupes)
        search_string = prop + '__exact'
        for dup in dupes:
            dupresults = Result.objects.prefetch_related('result_type').filter(**{search_string: dup[prop]}).all()
            delq = []
            keep = None
            for dpres in dupresults:
                if not keep:
                    keep = dpres
                    continue
                else:
                    error = False
                    if dpres.get_children():
                        try:
                            reparent_children(dpres, keep)
                        except Exception as exp:
                            printtf('Cannot reparent from Object {}, id={}'.format(dpres, dpres.id))
                            error = True
                    if relates_to_anything(dpres):
                        try:
                            update_relationships(dpres, keep)
                        except Exception as exp:
                            printtf('Cannot remove Object {}, id={}'.format(dpres, dpres.id))
                            error = True
                    if error:
                        printtf("ERROR OCCURED ON RECORD", dpres.id, dpres)
                        continue
                    delq.append(dpres)
            time.sleep(0.3)
            if not len(delq):
                printtf("Nothing is getting removed for {}".format(dupes))
            else:
                # delete everyting in the queue
                [i.delete() for i in delq]
                printtf("deleting: ", delq)
    # get all duplicates that have the same wbs
    dupes = Result.objects.values('wbs').annotate(Count('wbs')).order_by().filter(wbs__count__gt=1, wbs__isnull=False).exclude(wbs__exact='').all()
    dupes = sorted(dupes, key=lambda x: x['wbs'].count('/'), reverse=True)
    _run_clean('wbs', dupes)
    # get all duplicates that have a null wbs but same names
#    printtf("GETTING ALL DUPLICATES FOR RESULTS WITHOUT WBSS")
#    dupes = Result.objects.values('wbs', 'name').annotate(Count('name')).order_by().filter(name__count__gt=1, wbs__isnull=True).filter(Q(wbs__isnull=True) | Q(wbs__exact='')).all()
#    _run_clean('name', dupes)


#execute first
def fix_string_wbs():
    results = Result.objects.filter(wbs__exact='').all()
    for res in results:
        res.wbs = None
        res.save()

def fix_indicator_code():
    indicators = Indicator.objects.filter(code__exact='').all()
    for ind in indicators:
        ind.code = None
        ind.save()

    time.sleep(3)




def get_cpwbs(wbs):
    grp = wbs.split('/')
    return '/'.join(grp[:3])


def cp_fix(country_name):
    if not country_name:
        printtf("country name required /n")
    set_country(country_name)

    results = Result.objects.filter(wbs__isnull=False).exclude(wbs__exact='')
    locpwbs = []
    for res in results:
        cpwbs = get_cpwbs(res.wbs)
        if cpwbs not in locpwbs:
            locpwbs.append(cpwbs)

    today = datetime.now()
    for i in range(len(locpwbs)):
        today = today + timedelta(days=i)
        tomorrow = today + timedelta(days=365)
        cp, created = CountryProgramme.objects.get_or_create(wbs=locpwbs[i], name='Country Programme '+str(i), from_date=today, to_date=tomorrow)

    time.sleep(5)

    for res in results:
        cp = CountryProgramme.objects.get(wbs=get_cpwbs(res.wbs))
        res.country_programme = cp
        res.save()



def up_cp_first(n):
    if not n:
        print('add a number greater than 100 for all')
        return
    for cntry in Country.objects.order_by('name').all():
        n-=1
        if n==0:
            break
        if cntry.name in ['Global']:
            continue
        printtf("Updating  CPs for {}".format(cntry.name))
        cp_fix(cntry.name)


def up_indicators(n):
    if not n:
        print('add a number greater than 100 for all')
        return
    for cntry in Country.objects.order_by('name').all():
        n-=1
        if n==0:
            break
        if cntry.name in ['Global']:
            continue
        printtf("Updating results for {}".format(cntry.name))
        fix_duplicate_indicators(cntry.name)

def up_results(n):
    if not n:
        print('add a number greater than 100 for all')
        return
    for cntry in Country.objects.order_by('name').all():
        n-=1
        if n==0:
            break
        if cntry.name in ['Global']:
            continue
        printtf("Updating results for {}".format(cntry.name))
        fix_duplicate_results(cntry.name)


def clean_all():
    # Cleaning results for all countries
    up_results(100)

    # Adding country progrmmes in each country based on results
    up_cp_first(100)

    # clean Indicators
    up_indicators(100)


