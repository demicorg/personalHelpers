import streamlit as st

MEALS = {
    "Snidane": {
        "proteins": [
            {"name": "150g cottage", "fat_allowed": True},
            {"name": "140g milko svacinka", "fat_allowed": True},
            {"name": "250ml kefiroveho mleka", "fat_allowed": True},
            {"name": "100-150g tvarohu", "fat_allowed": True},
            {"name": "140g skyru", "fat_allowed": True},
            {"name": "150-200g protein puding", "fat_allowed": True},
            {"name": "75g jogurt + 10g protein", "fat_allowed": True},
            {"name": "100g tofu natural", "fat_allowed": True},
            {"name": "2 vejce", "fat_allowed": False},
            {"name": "70g 30% syru", "fat_allowed": False},
            {"name": "1 vejce + 75g cottage", "fat_allowed": False},
            {"name": "1 vehce + 30-40g syru", "fat_allowed": False},
            {"name": "1 vejce + 50g tofu", "fat_allowed": False},
            {"name": "100g ochuceneho tofu", "fat_allowed": False},
            {"name": "150g pomazanka z tvarohu/skyru, vejce/syru + trochu oleje", "fat_allowed": False},
            {"name": "150-200g jogurtu", "fat_allowed": False}
        ],
        "carbs": ["40g vlocek", "40g kase", "80-90g peciva"],
        "fats": [
            "lzice oleje",
            "10g masla",
            "40g avokada",
            "30g syru",
            "30g cream cheese/ricotta",
            "50g zakysanky",
            "lzice seminek",
            "10-15g orechu nebo orechoveho masla",
            "20g orechoveho proteinu",
            "15g horka cokolada",
            "50g Lunter pomazanka (nebo jina kolem 15% tuku)",
            "50g lucina linie, zerve light",
            "30g lucina, zerve, philadephia",
            "30g Patifu pomazanka"
            ]
    },
    "Svaca": {
        "fixed_meals": [
            "20-30g proteinu + 200ml oves/ryzovy napoj + lzicka arasidoveho masla + 1/2 mene zraleho bananu + lzicka kakaa",
            "30g praskoveho arasidoveho masla + 10g chia + 200ml ryzoveho napoje + maliny",
            "20-30g proteinu + voda + hrst boruvek + 2 lzice vlocek",
            "2 lzice vlocek (semix, cornflakes) + 150-200g  bileho jogurtu",
            "2 lzice vlocek + 80g tvarohu + holandske kakao + 1/2 mene zraleho bananu + 1 lzicka arasidoveho masla",
            "20g cornflakes + 150ml kokosoveho napoje Alpro + 15g proteinu",
            "200g jahod + 150g bily jogurt + 3ks makadamia nut",
            "hrst malin + 150g tvaroh + 2 lzice pohankovych vlocek + lzicka lneneho oleje",
            "1 ks protein drink Ehrmann/Milbona + 10g makadamovych orechu",
            "1 ks protein pudink + mene zraly banan",
            "150-200g cottage + okurka",
            "1/2 baleni cottage + 30g crispins tycinky",
            "2 lzice chia + 100ml kokosoveho mleka light z plechovky + 10g proteinu + ananas/jahody",
            "1 ks Ehrmann protein pudink + kus ovoce / hrst jahod",
            "1 ks Ehrmann protein pudink + 2 mandarinky",
            "330ml jogurtoveho napoje + 2 mandarinky + 10g makadamiovych orechu",
            "20g orechu",
            "kus/hrst ovoce",
            "miska zeleniny se lzickou zalivky",
            "miska polevky (dynova, spenatova, vyvar s tofu a nudlemi)",
            "100% ovocny sorbet",
            "30g pohankove krehke platky (Crispins) + 40g Leerdammer light + okurka",
            "50g pohankovy chleb + 20g Luciny + 2 platky Krolewski light + redkvicky",
            "50g bzl chleba + 30g ricotta + 40g uzene tofu + polnicek",
            "50g bzl chleba + 1 vejce + 30g Luciny + ledovy salat",
            "50g chleba + gervais + 2 platky 30% syru + okurka",
            "50g chleba + 1 vejce + 30g ricotta + kedlubna",
            "50g chleba + 2  platky uzeneho syru + lzice hummusu + rajce",
            "50g chleba + 1/2 hermelin light + zelenina",
            "50g chleba + pomazanka z 1/2 vejce + 50g tvarohu + zelenina",
            "50g chleba + 50g tvarohova pomazanka domaci + platek 30% syra",
            "50g chleba + 50g smakoun + 30g zerve fit + rajce",
            "3 krehke platky + 80g tvarohove pomazanky",
            "3 krehke platky + 30 platky 30% syru",
            "3 krehke platky + 1/2 baleni Milko svacinka",
            "1/2 baleni Crispins tycinek + 80g tvarohove pomazanky",
            "1/2 cizrny / fazoli + koreni + lzicka oleje",
            "tretina porce jidla od obeda / vecere",
            "4 lusteninove krehke platky + zelenina",
            "2-3 lzice vlocek / lupinku + kelimek jogurtu + kus ovoce",
            "2-3 lzice vlocek / lupinku + 250ml kefiru + hrst jahod",
            "2-3 lzice vlocek / lupinku + 250ml podmasli + kus ovoce + lzicka chia",
            "1 baleni (60g) instantni proteinove kase (Semix, Natural protein, Bombus)",
            "500ml kefiru, zakysu, jogurtoveho napoje, podmasli",
            "1 baleni Activia napoj bez cukru",
            "300ml kefir + pomeranc"

        ]
    },

    "Obed / Vecere": {
        "proteins": [
            {"name": "200g cottage", "fat_allowed": True},
            {"name": "200-250g tvaroh", "fat_allowed": True},
            {"name": "140g milko svacinka + 40g 30% syru", "fat_allowed": True},
            {"name": "150g nudlicky Garden Gourmet", "fat_allowed": True},
            {"name": "30-40g sojove/hrachove maso suche", "fat_allowed": True},
            {"name": "50g cervena cocka + 15g praskovy seitan", "fat_allowed": True},
            {"name": "20g sojove maso suche + 15g praskovy seitan", "fat_allowed": True},
            {"name": "20g sojove maso suche + 1/2 vejce + 20g 30% syru (placicky)", "fat_allowed": True},
            {"name": "20g sojove maso suche + 100g varena cizrna", "fat_allowed": True},
            {"name": "150g nahrazky masa s 15-20% bilkovin, do 10% tuku", "fat_allowed": True},
            {"name": "100g nahrazky do 10% tuku + 70g cottage", "fat_allowed": True},
            {"name": "100g nahrazky do 10% tuku + 80g varene lusteniny", "fat_allowed": True},
            {"name": "100g nahrazky do 10% tuku + 60g tofu", "fat_allowed": True},
            {"name": "100-150g lupinovy tempeh", "fat_allowed": True},
            {"name": "170g cockovy tempeh (o 1/3 mene prilohy)", "fat_allowed": True},
            {"name": "150g seitan", "fat_allowed": True},
            {"name": "100g seitan + 80g varena cizrna", "fat_allowed": True},
            {"name": "150-180g tofu natural", "fat_allowed": True},
            {"name": "200g smakoun", "fat_allowed": True},
            {"name": "100g smakoun + 90g tofu", "fat_allowed": True},
            {"name": "100g smakoun + 30g balkansky syr + 50g varena cizrna", "fat_allowed": True},
            {"name": "30-40g protein", "fat_allowed": True},
            {"name": "100g syru s 30% tuku", "fat_allowed": False},
            {"name": "3 vejce", "fat_allowed": False},
            {"name": "2 vejce + 70g cottage", "fat_allowed": False},
            {"name": "2 vejce + 35g niva fit", "fat_allowed": False},
            {"name": "120g mozzarella light + 50g cizrny", "fat_allowed": False},
            {"name": "120g mozzarella light + 20g parmazan", "fat_allowed": False},
            {"name": "160g mozzarella light", "fat_allowed": False},
            {"name": "100g syrove nite (+ 60g tofu)", "fat_allowed": False},
            {"name": "50g tempeh + 120g varena cizrna", "fat_allowed": False},
            {"name": "50g + 120g tofu", "fat_allowed": False},
            {"name": "150g tempeh Sojaprodukt (mene tucny)", "fat_allowed": False},
            {"name": "150g nahrazky masa s 15-20% bilkovin, 10-15% tuku", "fat_allowed": False}],
        "carbs": [
            "80-90g testovin",
            "80-90g quinoy",
            "80-90g ryze",
            "80-90g ryzovych nudli",
            "250-300g brambor",
            "250-300g batatu",
            "120g peciva"
            ],
        "fats":  [
            "lzice oleje",
            "10g masla",
            "40g avokada",
            "30g syru",
            "30g cream cheese/ricotta",
            "50g zakysanky",
            "lzice seminek",
            "10-15g orechu nebo orechoveho masla",
            "20g orechoveho proteinu",
            "15g horka cokolada",
            "50g Lunter pomazanka (nebo jina kolem 15% tuku)",
            "50g lucina linie, zerve light",
            "30g lucina, zerve, philadephia",
            "30g Patifu pomazanka"
            ]
    }
}

meal_type = st.selectbox("Typ jidla", list(MEALS.keys()))
meal = MEALS[meal_type]

if "fixed_meals" in meal:
    # -------------------
    # SVACA
    # -------------------
    selected_meal = st.selectbox(
        "Vyber svacinu",
        meal["fixed_meals"]
    )

    st.subheader("Tvoje svacina")
    st.write(selected_meal)

else:
    # -------------------
    # PROTEIN
    # -------------------
    protein_names = [p["name"] for p in meal["proteins"]]

    selected_protein_name = st.selectbox("Protein", protein_names)

    protein = next(
        p for p in meal["proteins"]
        if p["name"] == selected_protein_name
    )

    # -------------------
    # CARB
    # -------------------
    selected_carb = st.selectbox("Sacharid", meal["carbs"])

    # -------------------
    # FAT
    # -------------------
    fat_options = meal["fats"]

    if protein["fat_allowed"]:
        selected_fat = st.selectbox(
            "Tuk",
            ["Vyber si!"] + fat_options
        )

        if selected_fat == "Vyber si!":
            selected_fat = None
    else:
        st.warning("K tomuhle proteinu uz max jen lzicku oleje.")
        selected_fat = None

    # -------------------
    # FINAL OUTPUT
    # -------------------
    st.subheader("Tvuj pokrm")

    st.write("Protein:", protein["name"])
    st.write("Sacharid:", selected_carb)

    if selected_fat:
        st.write("Tuk:", selected_fat)