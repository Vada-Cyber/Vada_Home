import math

class LTETunnelCalculator:
    """
    LTE სიგნალის გავრცელების, დაფარვის და Link Budget გამოთვლა 
    გვირაბებში (საავტომობილო, მეტროს, სარკინიგზო)
    """
    
    def __init__(self):
        # LTE მოდულაციის ტიპები და მათი პარამეტრები
        self.modulation_schemes = {
            'QPSK': {'bits_per_symbol': 2, 'coding_rate': 0.5, 'SINR_req': -1},
            '16QAM': {'bits_per_symbol': 4, 'coding_rate': 0.5, 'SINR_req': 9},
            '64QAM': {'bits_per_symbol': 6, 'coding_rate': 0.75, 'SINR_req': 16},
            '256QAM': {'bits_per_symbol': 8, 'coding_rate': 0.9, 'SINR_req': 22}
        }
        
        # გვირაბის ტიპები და მათი პარამეტრები
        self.tunnel_types = {
            'საავტომობილო': {'width': 10, 'height': 5, 'roughness': 0.03},
            'მეტრო': {'width': 6, 'height': 4, 'roughness': 0.02},
            'სარკინიგზო': {'width': 8, 'height': 6, 'roughness': 0.025}
        }
    
    def free_space_path_loss(self, distance_km, frequency_mhz):
        """
        Free Space Path Loss (FSPL)
        FSPL(dB) = 32.45 + 20*log10(d_km) + 20*log10(f_MHz)
        """
        if distance_km <= 0 or frequency_mhz <= 0:
            return 0
        
        fspl = 32.45 + 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz)
        return fspl
    
    def tunnel_path_loss(self, distance_m, frequency_mhz, tunnel_type):
        """
        გვირაბში Path Loss გამოთვლა (Tunnel Propagation Model)
        PL = FSPL + α*d + β
        სადაც α - დამატებითი დაქსაქსუნება მეტრზე
        β - გვირაბის სტრუქტურის კორექცია
        """
        distance_km = distance_m / 1000
        
        # Free Space Path Loss
        fspl = self.free_space_path_loss(distance_km, frequency_mhz)
        
        # გვირაბის პარამეტრები
        params = self.tunnel_types.get(tunnel_type, self.tunnel_types['საავტომობილო'])
        width = params['width']
        height = params['height']
        roughness = params['roughness']
        
        # დამატებითი დაქსაქსუნება გვირაბში (dB/m)
        wavelength = 3e8 / (frequency_mhz * 1e6)  # მეტრებში
        alpha = 0.5 + 0.1 * roughness * (frequency_mhz / 1000)
        
        # გვირაბის კვეთის ფართობის გავლენა
        cross_section = width * height
        beta = 10 * math.log10(cross_section / 40)  # ნორმალიზაცია 40 m² ფართობზე
        
        # საერთო Path Loss
        path_loss = fspl + alpha * distance_m + beta
        
        return path_loss
    
    def calculate_uplink_budget(self, tx_power_dbm, frequency_mhz, distance_m, 
                                tunnel_type, modulation='QPSK'):
        """
        Uplink Link Budget გამოთვლა (UE -> eNodeB)
        
        პარამეტრები:
        - tx_power_dbm: UE გადამცემი სიმძლავრე (dBm), ჩვეულებრივ 23 dBm
        - frequency_mhz: სიხშირე MHz-ში
        - distance_m: მანძილი მეტრებში
        - tunnel_type: გვირაბის ტიპი
        - modulation: მოდულაციის ტიპი
        """
        
        # Path Loss
        path_loss = self.tunnel_path_loss(distance_m, frequency_mhz, tunnel_type)
        
        # UE პარამეტრები
        ue_antenna_gain = 0  # dBi
        
        # eNodeB პარამეტრები
        enodeb_antenna_gain = 8  # dBi (გვირაბში ჩვეულებრივ)
        enodeb_noise_figure = 3  # dB
        
        # თერმული ხმაური
        bandwidth_hz = 10e6  # 10 MHz LTE
        thermal_noise = -174 + 10 * math.log10(bandwidth_hz)  # dBm
        noise_power = thermal_noise + enodeb_noise_figure
        
        # მიღებული სიგნალის სიმძლავრე eNodeB-ზე
        rx_power = tx_power_dbm + ue_antenna_gain + enodeb_antenna_gain - path_loss
        
        # SINR
        sinr = rx_power - noise_power
        
        # საჭირო SINR მოდულაციისთვის
        required_sinr = self.modulation_schemes[modulation]['SINR_req']
        
        # Link Margin
        link_margin = sinr - required_sinr
        
        return {
            'TX Power (dBm)': tx_power_dbm,
            'Path Loss (dB)': round(path_loss, 2),
            'RX Power (dBm)': round(rx_power, 2),
            'Noise Power (dBm)': round(noise_power, 2),
            'SINR (dB)': round(sinr, 2),
            'Required SINR (dB)': required_sinr,
            'Link Margin (dB)': round(link_margin, 2),
            'Status': 'OK ✓' if link_margin > 0 else 'FAIL ✗'
        }
    
    def calculate_downlink_budget(self, tx_power_dbm, frequency_mhz, distance_m, 
                                  tunnel_type, modulation='64QAM'):
        """
        Downlink Link Budget გამოთვლა (eNodeB -> UE)
        
        პარამეტრები:
        - tx_power_dbm: eNodeB გადამცემი სიმძლავრე (dBm), ჩვეულებრივ 46 dBm
        - frequency_mhz: სიხშირე MHz-ში
        - distance_m: მანძილი მეტრებში
        - tunnel_type: გვირაბის ტიპი
        - modulation: მოდულაციის ტიპი
        """
        
        # Path Loss
        path_loss = self.tunnel_path_loss(distance_m, frequency_mhz, tunnel_type)
        
        # eNodeB პარამეტრები
        enodeb_antenna_gain = 8  # dBi
        
        # UE პარამეტრები
        ue_antenna_gain = 0  # dBi
        ue_noise_figure = 9  # dB
        
        # თერმული ხმაური
        bandwidth_hz = 10e6  # 10 MHz
        thermal_noise = -174 + 10 * math.log10(bandwidth_hz)
        noise_power = thermal_noise + ue_noise_figure
        
        # მიღებული სიგნალის სიმძლავრე UE-ზე
        rx_power = tx_power_dbm + enodeb_antenna_gain + ue_antenna_gain - path_loss
        
        # SINR
        sinr = rx_power - noise_power
        
        # საჭირო SINR მოდულაციისთვის
        required_sinr = self.modulation_schemes[modulation]['SINR_req']
        
        # Link Margin
        link_margin = sinr - required_sinr
        
        return {
            'TX Power (dBm)': tx_power_dbm,
            'Path Loss (dB)': round(path_loss, 2),
            'RX Power (dBm)': round(rx_power, 2),
            'Noise Power (dBm)': round(noise_power, 2),
            'SINR (dB)': round(sinr, 2),
            'Required SINR (dB)': required_sinr,
            'Link Margin (dB)': round(link_margin, 2),
            'Status': 'OK ✓' if link_margin > 0 else 'FAIL ✗'
        }
    
    def calculate_max_coverage(self, tx_power_dbm, frequency_mhz, tunnel_type, 
                               modulation, link_type='downlink'):
        """
        მაქსიმალური დაფარვის მანძილის გამოთვლა
        """
        # ბინარული ძიება მაქსიმალური დაფარვისთვის
        min_distance = 10  # მინ 10 მეტრი
        max_distance = 5000  # მაქს 5 კმ
        
        while max_distance - min_distance > 1:
            mid_distance = (min_distance + max_distance) / 2
            
            if link_type == 'downlink':
                result = self.calculate_downlink_budget(
                    tx_power_dbm, frequency_mhz, mid_distance, tunnel_type, modulation
                )
            else:
                result = self.calculate_uplink_budget(
                    tx_power_dbm, frequency_mhz, mid_distance, tunnel_type, modulation
                )
            
            if result['Link Margin (dB)'] > 0:
                min_distance = mid_distance
            else:
                max_distance = mid_distance
        
        return round(min_distance, 2)
    
    def calculate_throughput(self, bandwidth_mhz, modulation, sinr_db):
        """
        მონაცემთა გადაცემის სიჩქარის გამოთვლა (თეორიული)
        """
        mod_params = self.modulation_schemes[modulation]
        required_sinr = mod_params['SINR_req']
        
        if sinr_db < required_sinr:
            return 0
        
        # Shannon-ის ფორმულა მოდიფიცირებული
        efficiency = mod_params['bits_per_symbol'] * mod_params['coding_rate']
        throughput_mbps = bandwidth_mhz * efficiency * 0.9  # 10% overhead
        
        return round(throughput_mbps, 2)


# გამოყენების მაგალითები
if __name__ == "__main__":
    calc = LTETunnelCalculator()
    
    print("=" * 70)
    print("LTE სიგნალის გაანგარიშება გვირაბებში")
    print("=" * 70)
    
    # პარამეტრები
    frequency = 1800  # MHz (LTE Band 3)
    distance = 100  # მეტრი
    
    # საავტომობილო გვირაბი - Downlink
    print("\n1. საავტომობილო გვირაბი - DOWNLINK (64QAM)")
    print("-" * 70)
    dl_result = calc.calculate_downlink_budget(
        tx_power_dbm=46,
        frequency_mhz=frequency,
        distance_m=distance,
        tunnel_type='საავტომობილო',
        modulation='64QAM'
    )
    for key, value in dl_result.items():
        print(f"{key:25}: {value}")
    
    # საავტომობილო გვირაბი - Uplink
    print("\n2. საავტომობილო გვირაბი - UPLINK (QPSK)")
    print("-" * 70)
    ul_result = calc.calculate_uplink_budget(
        tx_power_dbm=23,
        frequency_mhz=frequency,
        distance_m=distance,
        tunnel_type='საავტომობილო',
        modulation='QPSK'
    )
    for key, value in ul_result.items():
        print(f"{key:25}: {value}")
    
    # მეტროს გვირაბი
    print("\n3. მეტროს გვირაბი - DOWNLINK (16QAM)")
    print("-" * 70)
    metro_result = calc.calculate_downlink_budget(
        tx_power_dbm=46,
        frequency_mhz=frequency,
        distance_m=distance,
        tunnel_type='მეტრო',
        modulation='16QAM'
    )
    for key, value in metro_result.items():
        print(f"{key:25}: {value}")
    
    # მაქსიმალური დაფარვა
    print("\n4. მაქსიმალური დაფარვის მანძილი")
    print("-" * 70)
    for tunnel in ['საავტომობილო', 'მეტრო', 'სარკინიგზო']:
        max_dist = calc.calculate_max_coverage(
            tx_power_dbm=46,
            frequency_mhz=frequency,
            tunnel_type=tunnel,
            modulation='64QAM',
            link_type='downlink'
        )
        print(f"{tunnel:20}: {max_dist} მ")
    
    print("\n" + "=" * 70)