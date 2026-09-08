"""Seed data for the case library (spec section 4).

Each entry matches the CaseLibraryEntry schema. `region` is one or more
ISO 3166-1 alpha-2 codes (comma-separated), or "GLOBAL" for cases not
tied to a specific market. `date_occurred` is "YYYY-MM-DD" or "YYYY-MM".
"""

CASES = [
    {
        "phrase_or_concept": '"Tank Day" tumbler promotion on the anniversary of the Gwangju massacre',
        "region": "KR",
        "category": "historical",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["advertising", "pr"],
        "description": (
            "Starbucks Korea launched a large tumbler nicknamed 'SS Tank' and promoted 'Tank Day' on May 18, the anniversary of the 1980 Gwangju military crackdown that killed hundreds of pro-democracy protesters. The imagery of tanks on that specific date was widely seen as mocking the massacre's victims, forcing stores to close early amid backlash and calls for boycott."
        ),
        "source_url": "https://www.nbcnews.com/world/asia/starbucks-tank-day-ad-campaign-south-korea-backlash-rcna346856",
        "date_occurred": "2026-05-18",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": 'Nike SB Dunk Low sneaker nicknamed the "Black and Tan"',
        "region": "IE,GB,US",
        "category": "linguistic",
        "industry_tags": ["fashion"],
        "content_type_tags": ["pr"],
        "description": (
            "Nike's Guinness-and-Harp-inspired St. Patrick's Day sneaker was nicknamed the 'Black and Tan' online, echoing the name of the notorious British paramilitary force that terrorized Irish civilians in 1920-21. Irish and Irish-American groups objected to the term being used festively, and Nike apologized and clarified the shoe's official name was unrelated."
        ),
        "source_url": "https://newsfeed.time.com/2012/03/15/nike-apologizes-for-offensive-name/",
        "date_occurred": "2012-03-15",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "Ben & Jerry's \"Black and Tan\" St. Patrick's Day ice cream flavor",
        "region": "IE,US",
        "category": "linguistic",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["pr"],
        "description": (
            "Ben & Jerry's named a 2006 St. Patrick's Day ice cream flavor after the Guinness-and-pale-ale 'Black and Tan' drink, unaware to many Irish-Americans that the phrase also names the brutal British auxiliary police force deployed against Irish civilians in the War of Independence. The company faced criticism for trivializing a painful historical term."
        ),
        "source_url": "https://www.irishcentral.com/culture/entertainment/five-biggest-irish-american-advertising-fails-photos",
        "date_occurred": "2006-03",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": '"Live For Now Moments Anthem" ad with Kendall Jenner handing a police officer a Pepsi',
        "region": "US",
        "category": "recent_event",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["advertising"],
        "description": (
            "Pepsi's 2017 ad showed Kendall Jenner leaving a photoshoot to join a generic protest and defusing tension with police by handing an officer a can of Pepsi. It landed weeks after real Black Lives Matter protests against police shootings, and critics accused Pepsi of trivializing the movement's imagery for profit; Pepsi pulled the ad within 24 hours and apologized."
        ),
        "source_url": "https://www.nbcnews.com/news/nbcblk/pepsi-ad-kendall-jenner-echoes-black-lives-matter-sparks-anger-n742811",
        "date_occurred": "2017-04-04",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": '"DG Loves China" campaign video of a woman struggling to eat pizza and spaghetti with chopsticks',
        "region": "CN",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising", "social_media"],
        "description": (
            "Dolce & Gabbana's pre-show promotional videos featured a Chinese model comically fumbling with chopsticks while a mocking male voiceover in accented Mandarin condescended to her, seen as reinforcing racist stereotypes. The backlash intensified after leaked screenshots showed designer Stefano Gabbana allegedly insulting China, leading to boycotts, canceled retail listings, and the cancellation of D&G's Shanghai runway show."
        ),
        "source_url": "https://time.com/5462653/dolce-gabbana-apology-insensitive-china-ads/",
        "date_occurred": "2018-11-21",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": '"Coolest Monkey in the Jungle" hoodie modeled by a Black child',
        "region": "GB",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "H&M's UK website showed a young Black boy wearing a green hoodie reading 'coolest monkey in the jungle,' evoking a long history of racist imagery comparing Black people to monkeys. The photo triggered global outrage, celebrity boycotts (The Weeknd, G-Eazy), vandalized stores in South Africa, and a stock drop, prompting H&M to apologize and appoint a diversity lead."
        ),
        "source_url": "https://www.washingtonpost.com/news/business/wp/2018/01/08/hm-apologizes-for-showing-black-child-wearing-a-monkey-in-the-jungle-sweatshirt/",
        "date_occurred": "2018-01-08",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": "Facebook video of a Black woman removing her shirt to reveal a white woman underneath",
        "region": "US",
        "category": "imagery",
        "industry_tags": ["fmcg", "healthcare"],
        "content_type_tags": ["advertising", "social_media"],
        "description": (
            "A 3-second clip from a Dove body wash ad appeared to show a Black woman transforming into a white woman after using the product, evoking racist 19th/20th-century 'soap' advertising that depicted Black skin as dirty. Dove said the clip was taken out of context from a longer 3-woman sequence, but the backlash and boycott calls persisted despite its apology."
        ),
        "source_url": "https://www.washingtonpost.com/news/business/wp/2017/10/08/dove-ad-that-shows-a-black-woman-turning-herself-white-sparks-consumer-backlash/",
        "date_occurred": "2017-10-07",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": '"White is Purity" deodorant ad copy',
        "region": "GLOBAL",
        "category": "imagery",
        "industry_tags": ["fmcg", "healthcare"],
        "content_type_tags": ["advertising", "social_media"],
        "description": (
            "Nivea's Middle East Facebook page ran an ad for its 'Invisible for Black & White' deodorant with the tagline 'White is purity' over an image of a white-robed woman, which was immediately read as endorsing white supremacy and was celebrated on white-nationalist forums. Nivea pulled the ad and apologized, though critics noted it was not the brand's first race-related misstep."
        ),
        "source_url": "https://www.washingtonpost.com/news/business/wp/2017/04/05/niveas-white-is-purity-ad-campaign-didnt-end-well/",
        "date_occurred": "2017-04-04",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": "Used-car ad depicting a groom's mother physically inspecting the bride like a car",
        "region": "CN",
        "category": "imagery",
        "industry_tags": ["automotive"],
        "content_type_tags": ["advertising"],
        "description": (
            "An Audi China ad for its used-car division showed a mother-in-law grabbing a bride's nose, ears, and body at the wedding altar to 'approve' her, comparing choosing a wife to buying a used car. Chinese social media users called it demeaning and sexist, and Audi apologized and pulled the ad, launching an internal review."
        ),
        "source_url": "https://www.scmp.com/news/china/society/article/2103346/audi-apologises-insulting-ad-china-comparing-women-used-cars",
        "date_occurred": "2017-07-19",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": '"Women belong in the kitchen" International Women\'s Day tweet',
        "region": "GB",
        "category": "recent_event",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["social_media"],
        "description": (
            "Burger King UK opened an International Women's Day Twitter thread with the sexist trope 'Women belong in the kitchen,' intending to pivot into an announcement of a female chef scholarship program. Because the first tweet circulated without the follow-up context, it was seen as tone-deaf regardless of intent, and Burger King deleted it and apologized within 12 hours."
        ),
        "source_url": "https://www.washingtonpost.com/business/2021/03/08/burger-king-tweet-women/",
        "date_occurred": "2021-03-08",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"The Gift That Gives Back" holiday ad of a husband gifting his wife a Peloton bike',
        "region": "US",
        "category": "imagery",
        "industry_tags": ["fitness", "tech"],
        "content_type_tags": ["advertising"],
        "description": (
            "Peloton's 2019 holiday spot showed a slim, already-fit woman nervously filming a year of workouts on a Peloton her husband gave her, which many viewers read as depicting a woman being pressured to stay thin for her spouse. The ad went viral as 'sexist' and 'dystopian,' and Peloton's stock dropped roughly 9% amid the backlash."
        ),
        "source_url": "https://www.detroitnews.com/story/business/2019/12/03/peloton-backlash-gift-gives-ad-pummels-stock/40754625/",
        "date_occurred": "2019-11-26",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "American Apparel 'back to school' ad shot from a low, up-skirt angle on a schoolgirl-styled model",
        "region": "GB",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "American Apparel repeatedly ran hyper-sexualized ads, including a back-to-school social post photographed from behind and below a model in a school-style skirt, mimicking voyeuristic 'upskirt' photography. The UK's ASA banned it and several other American Apparel ads for sexualizing young-looking models and normalizing predatory imagery."
        ),
        "source_url": "https://www.marketingweek.com/american-apparel-ads-banned-for-normalising-predatory-sexual-behaviour/",
        "date_occurred": "2014-09-03",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"The Great Hunger" board game simulating the Irish Famine',
        "region": "IE",
        "category": "historical",
        "industry_tags": ["entertainment"],
        "content_type_tags": ["pr"],
        "description": (
            "A US-published board game about surviving the 19th-century Great Famine, in which players manage tenant-farmer families through the blight and emigration, was blasted by Irish listeners on national radio as 'insensitive' for gamifying a national trauma without historical consultation. Irish heritage bodies warned the product could 'do more harm than good' despite the creator's educational intent."
        ),
        "source_url": "https://www.thejournal.ie/board-game-irish-famine-divided-opinion-backlash-6928622-Jan2026",
        "date_occurred": "2026-01",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "Rising Sun flag imagery used in club/brand social media posts",
        "region": "KR,JP",
        "category": "historical",
        "industry_tags": [],
        "content_type_tags": ["social_media", "pr"],
        "description": (
            "Liverpool FC posted Club World Cup promotional images featuring the Japanese Rising Sun flag, a symbol Koreans associate with Imperial Japan's WWII-era militarism and colonial atrocities, comparable in offense to Nazi symbolism. South Korean fans reacted with anger and the club apologized and removed the imagery, part of a recurring pattern of brands unknowingly using the flag near Korean audiences."
        ),
        "source_url": "https://www.goal.com/en/news/liverpool-apology-club-world-cup-rising-sun-posts-korea/15hpyl038mmjx1oe1ytdma8q4m",
        "date_occurred": "2025-12",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "Children's striped shirt with a yellow six-pointed star badge",
        "region": "ES",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Zara sold a kids' T-shirt with blue-white stripes and a yellow sheriff-style star that many shoppers said closely resembled the striped uniforms and yellow Star of David badges forced on Jewish prisoners in Nazi concentration camps. Zara pulled the shirt within hours and apologized, its second such incident after a 2007 swastika-decorated handbag."
        ),
        "source_url": "https://www.nbcnews.com/pop-culture/viral/zara-pulls-kids-shirt-resembling-concentration-camp-uniform-apologizes-n190311",
        "date_occurred": "2014-08-27",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": 'Instagram ad clip of a giant white hand flicking a Black man into a shop named "Petit Colon"',
        "region": "DE",
        "category": "imagery",
        "industry_tags": ["automotive"],
        "content_type_tags": ["advertising", "social_media"],
        "description": (
            "A Volkswagen Golf ad on Instagram showed an oversized white hand shoving a Black man away and into a storefront reading 'Petit Colon' (French for 'little colonist/settler'), with animated letters some viewers read as spelling a German slur. VW apologized, calling the imagery unacceptable given the company's own history as a firm founded under the Nazi regime."
        ),
        "source_url": "https://www.cnn.com/2020/05/21/business/volkswagen-racist-ad-instagram",
        "date_occurred": "2020-05-20",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": 'Germany national team jersey number "44" resembling the SS Siegrune symbol',
        "region": "DE",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Adidas's font design for the number 44 on Germany's Euro 2024 football kit, when doubled, closely resembled the lightning-bolt 'SS' rune used by Nazi paramilitary units. Adidas and the German federation halted sales of personalized shirts bearing the number and redesigned it after public criticism, despite insisting the resemblance was unintentional."
        ),
        "source_url": "https://www.nbcnews.com/news/world/germany-soccer-jersey-barred-adidas-nazi-ss-lightning-symbol-rcna145977",
        "date_occurred": "2024-04-02",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Let\'s go Japan... the exact opposite of England" World Cup betting ad',
        "region": "IE,GB",
        "category": "linguistic",
        "industry_tags": ["gambling"],
        "content_type_tags": ["advertising"],
        "description": (
            "An Irish Paddy Power World Cup ad praised Japan as 'polite, organised, clean up after themselves' and called this 'the exact opposite of England,' playing on national stereotypes. Ireland's advertising watchdog banned it as demeaning and derogatory toward English people, part of the bookmaker's long history of deliberately provocative national-stereotype marketing."
        ),
        "source_url": "https://www.gbnews.com/news/world/paddy-power-ad-banned-racist-towards-english-people",
        "date_occurred": "2018-06",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": 'Mitsubishi SUV named "Pajero"',
        "region": "ES,MX",
        "category": "linguistic",
        "industry_tags": ["automotive"],
        "content_type_tags": [],
        "description": (
            "Mitsubishi's Pajero SUV, named after a wild Patagonian cat, is 'pajero' in Spanish — a common and deeply vulgar slang term for a man who masturbates. Mitsubishi sells the same vehicle as the 'Montero' throughout Spain and Latin America to avoid the unintended obscenity."
        ),
        "source_url": "https://en.wikipedia.org/wiki/Mitsubishi_Pajero",
        "date_occurred": "1982-01",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": 'Honda subcompact car originally planned as the "Honda Fitta"',
        "region": "SE,NO,DK",
        "category": "linguistic",
        "industry_tags": ["automotive"],
        "content_type_tags": ["advertising"],
        "description": (
            "Honda had finalized marketing materials and a slogan for its new subcompact under the name 'Fitta' before discovering, close to launch, that the word is a crude Swedish, Norwegian, and Danish term for female genitalia. Honda scrapped the name at the last minute, launching the car as the Honda Jazz in Europe and the Honda Fit in the US and Asia."
        ),
        "source_url": "https://www.carscoops.com/2007/09/why-honda-didnt-call-fit-jazz-by-its/",
        "date_occurred": "2001-06",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": 'Buick sedan named "LaCrosse"',
        "region": "CA",
        "category": "linguistic",
        "industry_tags": ["automotive"],
        "content_type_tags": [],
        "description": (
            "GM's Buick LaCrosse sedan carries a name that, in Quebec French slang, means to masturbate ('se crosser'). GM renamed the car 'Allure' for the Canadian market in 2005, though it later reverted to the LaCrosse name in 2010 to simplify North American marketing, betting Quebec buyers would associate it with the sport instead."
        ),
        "source_url": "https://www.cbc.ca/news/gm-faces-car-name-conundrum-1.775246",
        "date_occurred": "2005-01",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": 'Early ad-hoc Chinese transliterations of "Coca-Cola" reading as "bite the wax tadpole"',
        "region": "CN",
        "category": "linguistic",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["advertising"],
        "description": (
            "Before Coca-Cola registered an official Chinese trademark in 1928, independent shopkeepers created ad-hoc signage using Chinese characters that approximated the sound 'ko-ka-ko-la' but produced nonsensical or unappetizing meanings such as 'bite the wax tadpole.' Coca-Cola later solved this by researching and trademarking characters meaning 'to allow the mouth to rejoice' — a real but often-exaggerated case, since the bad transliterations were never Coke's own official marketing."
        ),
        "source_url": "https://www.snopes.com/fact-check/bite-the-wax-tadpole/",
        "date_occurred": "1928-01",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": 'Air Max 270 sole logo resembling the Arabic script for "Allah"',
        "region": "GB",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Muslim consumers said Nike's Air Max 270 stylized logo closely resembled the Arabic word for God, and objected to it appearing on a shoe sole that would be trodden in dirt; a UK petition demanding a global recall gathered over 14,000 signatures. Nike declined to recall the shoe, calling the resemblance unintentional, unlike a similar 1997 case where it withdrew 38,000 pairs and donated to an Islamic school."
        ),
        "source_url": "https://www.fastcompany.com/90300220/heres-why-thousands-of-muslims-want-nike-to-recall-the-air-max-270",
        "date_occurred": "2019-06",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Toy Series" holiday ad with children holding teddy bears in bondage-style leather harnesses',
        "region": "US",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Balenciaga's 2022 holiday campaign photographed young children posing with teddy-bear handbags dressed in BDSM-style leather harnesses, and a separate ad in the same campaign included a prop referencing a US Supreme Court case on child pornography law. The imagery triggered global outrage and boycott calls, celebrity distancing (including Kim Kardashian), and a formal apology from creative director Demna."
        ),
        "source_url": "https://www.nbcnews.com/news/europe/balenciaga-apologizes-kinky-ad-featuring-children-harness-wearing-tedd-rcna58532",
        "date_occurred": "2022-11-22",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": 'Interfaith baby-shower ad for the "Ekatvam" jewelry collection',
        "region": "IN",
        "category": "historical",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Tanishq's ad depicted a Muslim family hosting a traditional Hindu baby-shower ritual for their pregnant Hindu daughter-in-law, intended as a message of unity. Hindu nationalist social media users accused it of promoting 'love jihad,' a conspiracy theory alleging Muslim men convert Hindu women via marriage, and the ensuing harassment and store threats led Tanishq to withdraw the ad."
        ),
        "source_url": "https://edition.cnn.com/2020/10/13/india/tanishq-jewelry-commercial-india-scli-intl/index.html",
        "date_occurred": "2020-10-13",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": '"Rang Laaye Sang" Holi ad of a Hindu girl helping a Muslim boy reach the mosque',
        "region": "IN",
        "category": "historical",
        "industry_tags": ["fmcg"],
        "content_type_tags": ["advertising"],
        "description": (
            "A Surf Excel detergent ad for Holi showed a Hindu girl in white clothes shielding a Muslim boy from colored powder so he could reach namaaz on time, meant to celebrate interfaith harmony. Hindu nationalist critics accused Hindustan Unilever of privileging a Muslim ritual over the Hindu festival and trending #BoycottSurfExcel, while many others publicly defended the ad's message."
        ),
        "source_url": "https://www.thenewsminute.com/article/boycottsurfexcel-trends-twitter-after-hindu-muslim-harmony-ad-draws-flak-98105",
        "date_occurred": "2019-03",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Jashn-e-Riwaaz" Urdu name used for a Diwali-season clothing promotion',
        "region": "IN",
        "category": "linguistic",
        "industry_tags": ["fashion"],
        "content_type_tags": ["social_media"],
        "description": (
            "Retailer Fabindia promoted a festive collection using the Urdu phrase 'Jashn-e-Riwaaz' ('celebration of traditions') near Diwali, prompting right-wing accusations that a Hindu festival was being marketed with a phrase associated with Muslim/Persian linguistic heritage and 'Abrahamisation' of Hindu culture. Facing a boycott campaign, Fabindia deleted the post and clarified it was not actually its official Diwali collection name."
        ),
        "source_url": "https://www.aljazeera.com/news/2021/10/27/india-urdu-hindu-groups-hate-campaign-muslim-language-fabindia",
        "date_occurred": "2021-10-27",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "Balaclava sweater with an oversized red-lip cutout resembling blackface",
        "region": "US",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Gucci's $890 black turtleneck sweater pulled up to cover the lower face, with a cutout ringed in bright red around the mouth, was widely compared to blackface minstrelsy, and its release during Black History Month deepened the offense. Gucci pulled the item worldwide and apologized, following closely on similar 'blackface' controversies at Prada and Balmain."
        ),
        "source_url": "https://www.cnn.com/2019/02/07/us/gucci-blackface-sweater",
        "date_occurred": "2019-02-07",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": '"Pradamalia" monkey keychain figurine with oversized red lips',
        "region": "US",
        "category": "imagery",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Prada's window displays and $550 'Otto Toto' monkey keychains featured exaggerated red lips that a civil-rights attorney and social media users likened to blackface minstrel imagery reminiscent of 'Little Sambo' caricatures. Prada, unlike Dolce & Gabbana's defensive response to its own China scandal weeks later, quickly apologized, pulled the products, and pledged diversity training."
        ),
        "source_url": "https://time.com/5480583/prada-blackface/",
        "date_occurred": "2018-12-13",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": "Ashton Kutcher in brownface makeup playing a Bollywood producer",
        "region": "US",
        "category": "imagery",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["advertising"],
        "description": (
            "A Popchips online video ad had Ashton Kutcher play multiple 'international bachelors,' including an Indian character named Raj performed in brown makeup and an exaggerated accent. The brownface characterization drew immediate accusations of racism from commentators and comedians, and Popchips pulled the ad and apologized within days."
        ),
        "source_url": "https://abcnews.go.com/blogs/entertainment/2012/05/ashton-kutchers-popchips-ad-pulled-after-racist-outcry",
        "date_occurred": "2012-05-03",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Believe in something. Even if it means sacrificing everything" featuring Colin Kaepernick',
        "region": "US",
        "category": "recent_event",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Nike's 30th-anniversary 'Just Do It' campaign starred Colin Kaepernick, the NFL quarterback blackballed after kneeling during the national anthem to protest police brutality. The ad ignited immediate boycott threats and shoe-burning videos from critics who saw it as disrespecting the flag, while supporters praised the brand for backing racial-justice activism; Nike's stock and sales rose despite (and partly because of) the controversy."
        ),
        "source_url": "https://abcnews.go.com/Business/nikes-colin-kaepernick-campaign-controversial-brand-experts/story?id=57590454",
        "date_occurred": "2018-09-03",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": 'Super Bowl truck ad set to audio from Martin Luther King Jr.\'s "Drum Major Instinct" sermon',
        "region": "US",
        "category": "historical",
        "industry_tags": ["automotive"],
        "content_type_tags": ["advertising"],
        "description": (
            "Ram Trucks aired a Super Bowl LII ad using an excerpt of Dr. King's 1968 sermon about humility and service over footage promoting truck ownership and civic duty. Viewers and commentators criticized using a revered civil-rights figure's words to sell pickup trucks as commercially exploitative, and the King Center publicly distanced itself from the ad despite licensing having been secured from a separate King estate entity."
        ),
        "source_url": "https://www.washingtonpost.com/news/acts-of-faith/wp/2018/02/04/super-bowl-dodge-commercial-draws-backlash-for-using-a-sermon-from-the-rev-martin-luther-king-jr/",
        "date_occurred": "2018-02-04",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": 'Sponsored content celebrating trans influencer Dylan Mulvaney\'s "365 days of girlhood"',
        "region": "US",
        "category": "recent_event",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["social_media", "pr"],
        "description": (
            "Bud Light sent trans influencer Dylan Mulvaney a personalized can to mark one year since she began publicly identifying as a woman, which she featured in a sponsored social post. The brief partnership triggered a sustained conservative boycott that cost Bud Light its position as America's top-selling beer, while Mulvaney said the company's muted, unsupportive response left her exposed to harassment."
        ),
        "source_url": "https://en.wikipedia.org/wiki/Bud_Light_boycott",
        "date_occurred": "2023-04-01",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": '"Are You Beach Body Ready?" bikini ad on the London Underground',
        "region": "GB",
        "category": "imagery",
        "industry_tags": ["fitness", "healthcare"],
        "content_type_tags": ["advertising"],
        "description": (
            "Protein World's weight-loss supplement ad showed a bikini-clad model beside the question 'Are you beach body ready?', which critics said shamed women's bodies and promoted unrealistic standards. It drew a 40,000-signature petition, vandalized posters, and a #EachBodysReady counter-campaign, and the UK's ASA later banned it over unsubstantiated health claims."
        ),
        "source_url": "https://www.marketingweek.com/2015/04/29/controversial-beach-body-ad-banned-after-hundreds-of-complaints/",
        "date_occurred": "2015-04-29",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"We Believe: The Best Men Can Be" #MeToo-era ad confronting toxic masculinity',
        "region": "US",
        "category": "recent_event",
        "industry_tags": ["healthcare"],
        "content_type_tags": ["advertising"],
        "description": (
            "Gillette's rework of its 'The Best a Man Can Get' tagline showed men interrupting bullying, catcalling, and 'boys will be boys' excuses in the wake of #MeToo. The ad drew a wave of dislikes and boycott calls from viewers who felt it broadly indicted masculinity, even as others praised its message, making it one of the most polarizing brand-purpose ads of its era."
        ),
        "source_url": "https://www.cbsnews.com/news/gillette-commercial-backlash-razor-ad-challenging-images-of-masculinity-rubs-some-the-wrong-way-me-too/",
        "date_occurred": "2019-01-14",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"White is coming" billboard of a white woman gripping a Black woman\'s face',
        "region": "NL",
        "category": "imagery",
        "industry_tags": ["tech"],
        "content_type_tags": ["advertising"],
        "description": (
            "To launch a white-colored PSP console, Sony Netherlands ran a billboard of a pale-skinned woman firmly grabbing the chin of a dark-skinned woman, captioned 'White is coming.' Despite Sony's explanation that the campaign used many pairings to show console color contrast, the specific image was read as racially dominant and was pulled after criticism."
        ),
        "source_url": "https://www.engadget.com/2006-07-11-sony-pulls-controversial-psp-ads.html",
        "date_occurred": "2006-07-11",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Congrats, you survived the Boston Marathon!" finisher email',
        "region": "US",
        "category": "recent_event",
        "industry_tags": ["fitness", "fashion"],
        "content_type_tags": ["pr"],
        "description": (
            "Adidas, an official Boston Marathon sponsor, sent finishers a routine congratulatory email headlined 'you survived,' failing to account for the 2013 bombing at the same race that killed three people and injured hundreds. Runners and the public called the subject line grossly insensitive, and Adidas's CEO issued a personal apology."
        ),
        "source_url": "https://time.com/4745066/adidas-boston-marathon-email/",
        "date_occurred": "2017-04-18",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "Zero-emissions car ad depicting a failed suicide attempt by exhaust fumes",
        "region": "GB",
        "category": "imagery",
        "industry_tags": ["automotive"],
        "content_type_tags": ["advertising"],
        "description": (
            "A Hyundai ix35 online ad showed a man attempting suicide by piping car exhaust into a closed garage, framing the joke as him surviving because the model only emits water vapor. Mental health advocates and the public condemned trivializing suicide for a marketing punchline, and Hyundai pulled the video and apologized unreservedly."
        ),
        "source_url": "https://www.cnbc.com/2013/04/25/hyundai-apologizes-for-commercial-showing-attempted-suicide.html",
        "date_occurred": "2013-04-25",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": "Catalog images with women digitally removed for the Saudi edition",
        "region": "SA",
        "category": "imagery",
        "industry_tags": ["retail"],
        "content_type_tags": ["advertising"],
        "description": (
            "IKEA's Saudi Arabian catalog had women airbrushed out of scenes that were identical to the Swedish version — including removing a mother from a family bathroom scene and cutting a group of women from a dinner photo entirely. When Swedish media exposed the discrepancy, IKEA apologized, calling the omission a violation of its own values, and blamed its local franchisee."
        ),
        "source_url": "https://www.npr.org/sections/thetwo-way/2012/10/02/162139455/women-erased-from-ikeas-saudi-catalog-company-apologizes",
        "date_occurred": "2012-10-01",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Aunt Jemima" pancake mix name and mammy-caricature logo',
        "region": "US",
        "category": "brand",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["pr"],
        "description": (
            "Quaker Oats retired the 131-year-old Aunt Jemima brand, built on a minstrel-show character and slavery-era 'mammy' stereotype, renaming it Pearl Milling Company amid the 2020 racial-justice reckoning after George Floyd's death. The company explicitly acknowledged the brand's origins were rooted in racial stereotyping."
        ),
        "source_url": "https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/06/17/879104818/acknowledging-racial-stereotype-aunt-jemima-will-change-brand-name-and-image",
        "date_occurred": "2020-06-17",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Isis" bottle name on Dutch "Share a Coke" cans',
        "region": "NL",
        "category": "recent_event",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["advertising"],
        "description": (
            "Coca-Cola's personalized 'Share a Coke' bottles in the Netherlands printed the common Dutch girl's name 'Isis,' which by 2014 had become globally synonymous with the terrorist group dominating news headlines. Coca-Cola quietly withdrew the name from production to avoid the unintended and unwanted association."
        ),
        "source_url": "https://www.atlasobscura.com/articles/why-did-share-a-coke-blacklist-these-24-countries",
        "date_occurred": "2014-08",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": "China-market T-shirt map omitting Taiwan and the South China Sea",
        "region": "CN",
        "category": "historical",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "A Gap T-shirt printed with an outline map of China left out Taiwan and other disputed territories, and photos of it circulated on Chinese social media as an affront to China's territorial claims. Gap apologized, calling the map an 'error,' destroyed the affected stock, and pledged more rigorous review, joining a wave of Western brands forced to apologize for similar map slights."
        ),
        "source_url": "https://www.washingtonpost.com/news/worldviews/wp/2018/05/15/u-s-retailer-gap-apologizes-to-china-over-map-on-t-shirt-that-omits-taiwan-south-china-sea/",
        "date_occurred": "2018-05-15",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": 'Customer survey listing Tibet, Taiwan, Hong Kong, and Macau as separate "countries"',
        "region": "CN",
        "category": "historical",
        "industry_tags": ["travel"],
        "content_type_tags": ["pr"],
        "description": (
            "A Marriott loyalty-program survey asked members which 'country' they lived in, offering Tibet, Taiwan, Hong Kong, and Macau as options alongside sovereign states, which Chinese regulators and social media treated as challenging China's territorial claims. Marriott apologized, disciplined an employee who separately 'liked' a pro-Tibet tweet, and had its Chinese website and app briefly shut down by authorities."
        ),
        "source_url": "https://www.cbsnews.com/news/marriott-apologizes-to-beijing-calling-taiwan-and-tibet-countries/",
        "date_occurred": "2018-01-11",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": 'T-shirt listing "Hong Kong-Hong Kong" and "Macau-Macau" as country-city pairs',
        "region": "CN",
        "category": "historical",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "A Versace T-shirt design paired global cities with their countries (e.g. 'New York-USA') but listed Hong Kong and Macau as their own countries rather than as part of China. The design went viral on Weibo, prompting a Chinese celebrity to drop her Versace contract and Donatella Versace to personally apologize, followed by similar apologies from Coach and Givenchy for comparable designs."
        ),
        "source_url": "https://edition.cnn.com/style/article/versace-loses-yang-mi-hong-kong-protest-t-shirt-intl-scli/index.html",
        "date_occurred": "2019-08-11",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Motivational Monday" Instagram post quoting the Dalai Lama',
        "region": "CN",
        "category": "historical",
        "industry_tags": ["automotive"],
        "content_type_tags": ["social_media"],
        "description": (
            "Mercedes-Benz posted an inspirational quote from the Dalai Lama — a figure Beijing considers a dangerous separatist — over a luxury car photo on Instagram (which is blocked in mainland China but still drew backlash via VPN users). Facing boycott threats, Mercedes' parent Daimler issued two rounds of apology, explicitly affirming it did not intend to challenge China's sovereignty over Tibet."
        ),
        "source_url": "https://www.cnbc.com/2018/02/06/mercedes-benz-apologizes-to-chinese-for-inspirational-dalai-lama-quote.html",
        "date_occurred": "2018-02-06",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "Public statement declining to source cotton from Xinjiang over forced-labor concerns",
        "region": "CN",
        "category": "recent_event",
        "industry_tags": ["fashion"],
        "content_type_tags": ["pr"],
        "description": (
            "A months-old H&M statement expressing concern over alleged Uyghur forced labor in Xinjiang cotton production resurfaced on Chinese social media right after Western governments sanctioned Chinese officials over Xinjiang human-rights abuses. State media and consumers called for a boycott, and H&M was pulled from major Chinese e-commerce and map apps virtually overnight, showing how old corporate language can suddenly collide with a live geopolitical flashpoint."
        ),
        "source_url": "https://edition.cnn.com/2021/03/25/business/hm-nike-xinjiang-cotton-boycott-intl-hnk/index.html",
        "date_occurred": "2021-03-24",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": "Willem Dafoe as Marilyn Monroe in a Super Bowl \"you're not you when you're hungry\" ad",
        "region": "US",
        "category": "imagery",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["advertising"],
        "description": (
            "Snickers' 2016 Super Bowl ad had actor Willem Dafoe recreate Marilyn Monroe's iconic 'Seven Year Itch' pose before locking lips with another man, played for shock/comedy about being 'not yourself' when hungry. LGBTQ advocacy voices and social media users criticized the gay-kiss punchline as playing gender and sexual identity for a joke, and Mars pulled the ad from future airings."
        ),
        "source_url": "https://www.cbsnews.com/news/snickers-kiss-super-bowl-ad-pulled/",
        "date_occurred": "2016-02-07",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": "WWI Christmas Truce short film used to sell a £1 chocolate bar",
        "region": "GB",
        "category": "historical",
        "industry_tags": ["retail"],
        "content_type_tags": ["advertising"],
        "description": (
            "Sainsbury's 2014 Christmas ad dramatized the 1914 Christmas Day truce between British and German soldiers, complete with a tie-in chocolate bar sold in stores. Over a hundred viewers complained it was disrespectful and historically distorted to commercialize a solemn wartime moment for retail promotion, sparking a broader debate about brands monetizing sensitive national history."
        ),
        "source_url": "https://www.marketingweek.com/sainsburys-christmas-ad-could-face-investigation-after-135-complaints/",
        "date_occurred": "2014-11-13",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": "Cricket ad showing a white fan offering fried chicken to Black West Indies supporters",
        "region": "AU,US",
        "category": "imagery",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["advertising"],
        "description": (
            "A KFC Australia cricket ad depicted an awkward white fan surrounded by boisterous Black West Indian supporters offering them a bucket of fried chicken to 'silence' them, which ran without complaint in Australia but triggered outrage in the US, where fried chicken is loaded with racist stereotyping history largely absent from Australian culture. KFC's US office apologized for 'any misinterpretation' and the ad was pulled."
        ),
        "source_url": "https://www.abc.net.au/news/2010-01-07/kfc-pulls-cricket-ad-amid-racism-claims/1201378",
        "date_occurred": "2010-01-07",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"Cheat on your girlfriend, not on your workout" gym poster',
        "region": "DE",
        "category": "imagery",
        "industry_tags": ["fitness", "fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "Reebok posters placed in partner gym locker rooms across Germany urged patrons to 'cheat on your girlfriend, not on your workout,' seemingly condoning infidelity as a punchline. Photos spread internationally on social media, driving global boycott calls even though the campaign had run only in Germany; Reebok apologized and removed the posters."
        ),
        "source_url": "https://www.npr.org/2012/03/22/149126035/reebok-slammed-for-cheat-on-your-girlfriend-ad",
        "date_occurred": "2012-03-22",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": 'CEO blog post using the anti-Korean slur "chontory" about a rival\'s ad models',
        "region": "JP,KR",
        "category": "linguistic",
        "industry_tags": ["healthcare"],
        "content_type_tags": ["pr", "social_media"],
        "description": (
            "DHC's Japanese CEO published a company blog post mocking a rival's ethnically Korean ad talent using 'chontory,' a slur combining a derogatory term for Koreans with the rival's name, and boasted DHC was a 'pure Japanese company.' The remarks triggered a sustained Korean boycott and protests, ultimately forcing DHC to exit the South Korean market entirely in 2021."
        ),
        "source_url": "https://globalvoices.org/2021/01/26/japanese-skincare-company-faces-online-backlash-and-boycott-after-ceos-racist-remarks/",
        "date_occurred": "2020-12",
        "severity_baseline": "high",
        "active": True,
    },
    {
        "phrase_or_concept": "Company chairman showing staff a video praising Japan's PM during a Korea-Japan trade dispute",
        "region": "KR,JP",
        "category": "historical",
        "industry_tags": ["healthcare"],
        "content_type_tags": ["pr"],
        "description": (
            "The Korean chairman of cosmetics firm Kolmar Korea (backed by Japan's Nihon Kolmar) played staff a YouTube video praising Japanese PM Shinzo Abe and criticizing Korea's own president during a bitter Korea-Japan trade and historical-grievance standoff. Korean consumers, sensitive to any perceived pro-Japan stance from a domestic company amid colonial-era tensions, launched boycott calls, and the chairman apologized."
        ),
        "source_url": "https://www.businessoffashion.com/news/news-analysis/korean-cosmetics-firm-in-hot-water-over-video-praising-japan-in-trade-row/",
        "date_occurred": "2019-08-09",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": '"fcuk" branding stylized to resemble an obscenity',
        "region": "GB",
        "category": "linguistic",
        "industry_tags": ["fashion"],
        "content_type_tags": ["advertising"],
        "description": (
            "French Connection UK built a deliberately provocative campaign around the acronym 'fcuk,' visually and phonetically evoking a profanity. The UK's ASA banned the inaugural 'fcuk fashion' poster campaign in 1997 as likely to cause serious or widespread offense, and complaints against the recurring near-obscene branding topped 500 by 2003, with a related US magazine ad pulled after parent complaints in Tennessee schools."
        ),
        "source_url": "https://en.wikipedia.org/wiki/French_Connection_(clothing)",
        "date_occurred": "1997-07",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": 'Mobile wallet product named "Isis"',
        "region": "US",
        "category": "brand",
        "industry_tags": ["fintech"],
        "content_type_tags": ["pr"],
        "description": (
            "A joint AT&T/T-Mobile/Verizon mobile-payments venture had been branded 'Isis,' after the Egyptian goddess, since 2010 — but as the Islamic State terror group (also called ISIS) dominated 2014 headlines, the wallet's name became an unavoidable and unwanted association. The company rebranded to 'Softcard,' with its CEO citing no interest in sharing a name synonymous with violence."
        ),
        "source_url": "https://www.cnbc.com/2014/09/03/isis-wallet-rebrands-to-softcard-to-avoid-confusion-with-militants.html",
        "date_occurred": "2014-09-03",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": '"Uncle Ben\'s" rice brand and bow-tied elderly Black man logo',
        "region": "US",
        "category": "brand",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["pr"],
        "description": (
            "Mars retired the 70-year-old Uncle Ben's rice brand, whose logo of a deferential elderly Black man in a bow tie was widely criticized as perpetuating the 'faithful servant' racial trope common in Jim Crow-era advertising. The brand relaunched as 'Ben's Original' with the caricature logo dropped entirely, part of a wave of legacy food-brand overhauls following the 2020 racial-justice protests."
        ),
        "source_url": "https://www.washingtonpost.com/news/voraciously/wp/2020/09/23/uncle-bens-brand-evolves-into-bens-original-after-criticism-of-racial-stereotyping/",
        "date_occurred": "2020-09-23",
        "severity_baseline": "medium",
        "active": True,
    },
    {
        "phrase_or_concept": "Land O'Lakes packaging logo of a kneeling Native American woman",
        "region": "US",
        "category": "brand",
        "industry_tags": ["food_beverage"],
        "content_type_tags": ["pr"],
        "description": (
            "Land O'Lakes quietly dropped 'Mia,' its nearly-century-old logo of a kneeling Native American woman, from butter and dairy packaging after long-running criticism that the image was a demeaning caricature and form of cultural appropriation, even though some Native commentators saw it differently as a source of pride. The company replaced it with a lake-and-farmland scene and made no public mention of removing the figure."
        ),
        "source_url": "https://www.cnn.com/2020/04/17/us/landolakes-logo-change-trnd",
        "date_occurred": "2020-04-17",
        "severity_baseline": "low",
        "active": True,
    },
    {
        "phrase_or_concept": '"Monsanto" corporate name retired after Bayer acquisition',
        "region": "US",
        "category": "brand",
        "industry_tags": ["agriculture"],
        "content_type_tags": ["pr"],
        "description": (
            "After completing its $63 billion purchase of Monsanto, German pharmaceutical and agriculture giant Bayer announced it would drop the Monsanto name entirely, folding its products into the Bayer brand. The decision was explicitly reputational: Monsanto ranked near the bottom of US corporate-reputation rankings due to GMO controversy and Roundup litigation, and Bayer wanted the products without the baggage attached to the name."
        ),
        "source_url": "https://www.cbsnews.com/news/bayer-monsanto-merger-closes-a-toxic-corporate-name-to-be-retired/",
        "date_occurred": "2018-06-07",
        "severity_baseline": "low",
        "active": True,
    },
]
