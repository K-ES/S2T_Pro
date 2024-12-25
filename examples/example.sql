WITH
    -- CTE 1
    cte_players AS (
        SELECT * FROM game_db.players
    ),
    -- CTE 2
    cte_active_players AS (
        SELECT * FROM cte_players WHERE status = 'Active'
    ),
    -- CTE 3
    cte_games AS (
        SELECT * FROM game_db.games
    ),
    -- CTE 4
    cte_sales AS (
        SELECT * FROM game_db.sales
    ),
    -- CTE 5
    cte_ratings AS (
        SELECT * FROM game_db.ratings
    ),
    -- CTE 6
    cte_genres AS (
        SELECT * FROM game_db.genres
    ),
    -- CTE 7
    cte_platforms AS (
        SELECT * FROM game_db.platforms
    ),
    -- CTE 8
    cte_reviews AS (
        SELECT * FROM game_db.reviews
    ),
    -- CTE 9
    cte_developers AS (
        SELECT * FROM game_db.developers
    ),
    -- CTE 10
    cte_publishers AS (
        SELECT * FROM game_db.publishers
    ),
    -- CTE 11
    cte_multiplayer_stats AS (
        SELECT * FROM game_db.multiplayer_stats
    ),
    -- CTE 12
    cte_singleplayer_stats AS (
        SELECT * FROM game_db.singleplayer_stats
    ),
    -- CTE 13
    cte_dlc AS (
        SELECT * FROM game_db.dlc
    ),
    -- CTE 14
    cte_updates AS (
        SELECT * FROM game_db.updates
    ),
    -- CTE 15
    cte_events AS (
        SELECT * FROM game_db.events
    ),
    -- CTE 16
    cte_tournaments AS (
        SELECT * FROM game_db.tournaments
    ),
    -- CTE 17
    cte_leaderboards AS (
        SELECT * FROM game_db.leaderboards
    ),
    -- CTE 18
    cte_achievements AS (
        SELECT * FROM game_db.achievements
    ),
    -- CTE 19
    cte_inventories AS (
        SELECT * FROM game_db.inventories
    ),
    -- CTE 20
    cte_virtual_items AS (
        SELECT * FROM game_db.virtual_items
    ),
    -- CTE 21
    cte_transactions AS (
        SELECT * FROM game_db.transactions
    ),
    -- CTE 22
    cte_rewards AS (
        SELECT * FROM game_db.rewards
    ),
    -- CTE 23
    cte_friends AS (
        SELECT * FROM game_db.friends
    ),
    -- CTE 24
    cte_messages AS (
        SELECT * FROM game_db.messages
    ),
    -- CTE 25
    cte_achieved_quests AS (
        SELECT * FROM game_db.achieved_quests
    ),
    -- CTE 26
    cte_active_quests AS (
        SELECT * FROM game_db.active_quests
    ),
    -- CTE 27
    cte_quest_rewards AS (
        SELECT * FROM game_db.quest_rewards
    ),
    -- CTE 28
    cte_user_settings AS (
        SELECT * FROM game_db.user_settings
    ),
    -- CTE 29
    cte_game_sessions AS (
        SELECT * FROM game_db.game_sessions
    ),
    -- CTE 30
    cte_session_logs AS (
        SELECT * FROM game_db.session_logs
    ),
    -- CTE 31
    cte_error_logs AS (
        SELECT * FROM game_db.error_logs
    ),
    -- CTE 32
    cte_performance_metrics AS (
        SELECT * FROM game_db.performance_metrics
    ),
    -- CTE 33
    cte_server_stats AS (
        SELECT * FROM game_db.server_stats
    ),
    -- CTE 34
    cte_user_feedback AS (
        SELECT * FROM game_db.user_feedback
    ),
    -- CTE 35
    cte_bug_reports AS (
        SELECT * FROM game_db.bug_reports
    ),
    -- CTE 36
    cte_feature_requests AS (
        SELECT * FROM game_db.feature_requests
    ),
    -- CTE 37
    cte_marketing_campaigns AS (
        SELECT * FROM game_db.marketing_campaigns
    ),
    -- CTE 38
    cte_advertisements AS (
        SELECT * FROM game_db.advertisements
    ),
    -- CTE 39
    cte_social_media_posts AS (
        SELECT * FROM game_db.social_media_posts
    ),
    -- CTE 40
    cte_affiliates AS (
        SELECT * FROM game_db.affiliates
    ),
    -- CTE 41
    cte_affiliate_sales AS (
        SELECT * FROM game_db.affiliate_sales
    ),
    -- CTE 42
    cte_affiliate_payments AS (
        SELECT * FROM game_db.affiliate_payments
    ),
    -- CTE 43
    cte_subscription_plans AS (
        SELECT * FROM game_db.subscription_plans
    ),
    -- CTE 44
    cte_user_subscriptions AS (
        SELECT * FROM game_db.user_subscriptions
    ),
    -- CTE 45
    cte_subscription_payments AS (
        SELECT * FROM game_db.subscription_payments
    ),
    -- CTE 46
    cte_referrals AS (
        SELECT * FROM game_db.referrals
    ),
    -- CTE 47
    cte_referral_rewards AS (
        SELECT * FROM game_db.referral_rewards
    ),
    -- CTE 48
    cte_loyalty_program AS (
        SELECT * FROM game_db.loyalty_program
    ),
    -- CTE 49
    cte_loyalty_points AS (
        SELECT * FROM game_db.loyalty_points
    ),
    -- CTE 50
    cte_loyalty_rewards AS (
        SELECT * FROM game_db.loyalty_rewards
    ),
    -- CTE 51
    cte_gamification AS (
        SELECT * FROM game_db.gamification
    ),
    -- CTE 52
    cte_badges AS (
        SELECT * FROM game_db.badges
    ),
    -- CTE 53
    cte_leaderboard_entries AS (
        SELECT * FROM game_db.leaderboard_entries
    ),
    -- CTE 54
    cte_user_progress AS (
        SELECT * FROM game_db.user_progress
    ),
    -- CTE 55
    cte_tutorials AS (
        SELECT * FROM game_db.tutorials
    ),
    -- CTE 56
    cte_tutorial_completion AS (
        SELECT * FROM game_db.tutorial_completion
    ),
    -- CTE 57
    cte_game_modes AS (
        SELECT * FROM game_db.game_modes
    ),
    -- CTE 58
    cte_game_mode_stats AS (
        SELECT * FROM game_db.game_mode_stats
    ),
    -- CTE 59
    cte_in_game_purchases AS (
        SELECT * FROM game_db.in_game_purchases
    ),
    -- CTE 60
    cte_purchase_history AS (
        SELECT * FROM game_db.purchase_history
    )

-- Финальный SELECT, выбирающий данные из различных CTE
SELECT
    cte_purchase_history.player_id AS player_id,
    cte_purchase_history.game_id AS game_id,
    cte_purchase_history.purchase_date AS purchase_date,
    cte_players.player_name AS player_name,
    cte_games.game_title AS game_title,
    cte_genres.genre_name AS genre,
    cte_platforms.platform_name AS platform,
    cte_ratings.rating AS game_rating,
    cte_sales.total_sales AS sales,
    cte_reviews.review_count AS review_count,
    cte_developers.developer_name AS developer,
    cte_publishers.publisher_name AS publisher,
    cte_achievements.achievement_name AS achievement,
    cte_leaderboards.rank AS leaderboard_rank,
    cte_achieved_quests.quest_id AS quest_id,
    cte_user_settings.language AS preferred_language,
    cte_game_sessions.session_duration AS session_duration,
    cte_error_logs.error_count AS error_count,
    cte_performance_metrics.fps AS frames_per_second,
    cte_user_feedback.feedback AS user_feedback,
    cte_marketing_campaigns.campaign_name AS marketing_campaign,
    cte_subscription_plans.plan_name AS subscription_plan,
    cte_referrals.referral_code AS referral_code,
    cte_loyalty_points.points AS loyalty_points,
    cte_tutorial_completion.completed AS tutorial_completed,
    cte_game_modes.mode_name AS game_mode,
    cte_in_game_purchases.item_id AS purchased_item
FROM
    cte_purchase_history
    JOIN cte_players ON cte_purchase_history.player_id = cte_players.player_id
    JOIN cte_games ON cte_purchase_history.game_id = cte_games.game_id
    JOIN cte_genres ON cte_games.genre_id = cte_genres.genre_id
    JOIN cte_platforms ON cte_games.platform_id = cte_platforms.platform_id
    JOIN cte_ratings ON cte_games.game_id = cte_ratings.game_id
    JOIN cte_sales ON cte_games.game_id = cte_sales.game_id
    JOIN cte_reviews ON cte_games.game_id = cte_reviews.game_id
    JOIN cte_developers ON cte_games.developer_id = cte_developers.developer_id
    JOIN cte_publishers ON cte_games.publisher_id = cte_publishers.publisher_id
    LEFT JOIN cte_achievements ON cte_purchase_history.player_id = cte_achievements.player_id
    LEFT JOIN cte_leaderboards ON cte_purchase_history.player_id = cte_leaderboards.player_id
    LEFT JOIN cte_achieved_quests ON cte_purchase_history.player_id = cte_achieved_quests.player_id
    LEFT JOIN cte_user_settings ON cte_purchase_history.player_id = cte_user_settings.player_id
    LEFT JOIN cte_game_sessions ON cte_purchase_history.player_id = cte_game_sessions.player_id
    LEFT JOIN cte_error_logs ON cte_purchase_history.player_id = cte_error_logs.player_id
    LEFT JOIN cte_performance_metrics ON cte_game_sessions.session_id = cte_performance_metrics.session_id
    LEFT JOIN cte_user_feedback ON cte_purchase_history.player_id = cte_user_feedback.player_id
    LEFT JOIN cte_marketing_campaigns ON cte_sales.campaign_id = cte_marketing_campaigns.campaign_id
    LEFT JOIN cte_subscription_plans ON cte_user_subscriptions.plan_id = cte_subscription_plans.plan_id
    LEFT JOIN cte_referrals ON cte_players.referral_id = cte_referrals.referral_id
    LEFT JOIN cte_loyalty_points ON cte_players.player_id = cte_loyalty_points.player_id
    LEFT JOIN cte_tutorial_completion ON cte_players.player_id = cte_tutorial_completion.player_id
    LEFT JOIN cte_game_modes ON cte_game_sessions.mode_id = cte_game_modes.mode_id
    LEFT JOIN cte_in_game_purchases ON cte_purchase_history.purchase_id = cte_in_game_purchases.purchase_id
WHERE
    cte_games.release_date BETWEEN '2023-01-01' AND '2024-12-31'
    AND cte_players.region = 'North America'
ORDER BY
    cte_purchase_history.purchase_date DESC;
