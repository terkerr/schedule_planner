SAMPLE_HTML = """
<div class="panel-body">
    <div class="row">
        <div class="col-sm-2">
            <span data-bind="text: maxCredits">Số tín chỉ tối đa:</span>
        </div>
        <div class="col-sm-1">
            <span data-bind="text: svDetails().SoTCMax">24</span>
        </div>
        <div class="col-sm-2">
            <span data-bind="text: maxSubject">Số môn học tối đa:</span>
        </div>
        <div class="col-sm-1">
            <span data-bind="text: svDetails().SoMonMax">6</span>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-2">
            <span data-bind="text: regCredits">Số tín chỉ đăng ký:</span>
        </div>
        <div class="col-sm-1">
            <span data-bind="text: svDetails().SoTCDaDK">0</span>
        </div>
        <div class="col-sm-2">
            <span data-bind="text: regSubject">Số môn đã đăng ký:</span>
        </div>
        <div class="col-sm-1">
            <span data-bind="text: svDetails().SoMonDaDK">0</span>
        </div>
    </div>
</div>
<table id="tblSinhVien" class="table table-striped table-bordered">
        <thead>
            <tr>
                <th class="text-center" style="width: 40px;">STT</th>
                <th class="text-center" style="width: 70px;">Mã MH</th>
                <th class="text-center">Tên MH</th>
                <th class="text-center" style="width: 100px;">Lớp</th>
                <th class="text-center" style="width: 60px;"><span data-bind="tooltip: { title: 'Số tín chỉ' }" data-original-title="" title="">Số TC</span></th>

                <th class="text-center" style="width: 100px;">Lịch LT</th>
                <th class="text-center" style="width: 100px;">Lịch TH</th>

                <th class="text-center" style="width: 40px;" data-bind="visible: svDetails().LoaiSV == 'CLC'">
                    <span data-bind="tooltip: { title: 'Học bằng Tiếng Anh' }" data-original-title="" title="">TA</span>
                </th>

                <th class="text-center" style="width: 70px;"><span data-bind="tooltip: { title: 'Số SV dự kiến' }" data-original-title="" title="">Dự kiến</span></th>
                <th class="text-center" style="width: 70px; display: none;" data-bind="visible: $root.ok">
                    <span data-bind="tooltip: { title: 'Số SV đã đăng ký' }" data-original-title="" title="">Đã ĐK</span>
                </th>

                
            </tr>
        </thead>
        <tbody data-bind="foreach: dsChuaDangKy">
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">1</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00103</td>
                <td class="text-left" data-bind="text: TenMH">Chủ nghĩa xã hội khoa học</td>
                <td class="text-center" data-bind="text: MaLopHP">24C01</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">100</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/100</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">2</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13002</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn công nghệ phần mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">24C01</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">3</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00103</td>
                <td class="text-left" data-bind="text: TenMH">Chủ nghĩa xã hội khoa học</td>
                <td class="text-center" data-bind="text: MaLopHP">24C02</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">100</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/100</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">4</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13002</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn công nghệ phần mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">24C02</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">5</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00103</td>
                <td class="text-left" data-bind="text: TenMH">Chủ nghĩa xã hội khoa học</td>
                <td class="text-center" data-bind="text: MaLopHP">24C03</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">100</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/100</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">6</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13002</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn công nghệ phần mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">24C03</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">7</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00103</td>
                <td class="text-left" data-bind="text: TenMH">Chủ nghĩa xã hội khoa học</td>
                <td class="text-center" data-bind="text: MaLopHP">24C04</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">100</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/100</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">8</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13002</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn công nghệ phần mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">24C04</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">9</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00103</td>
                <td class="text-left" data-bind="text: TenMH">Chủ nghĩa xã hội khoa học</td>
                <td class="text-center" data-bind="text: MaLopHP">24C05</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">100</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/100</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">10</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13002</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn công nghệ phần mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">24C05</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }" style="background-color: beige;">
                <td class="text-center" data-bind="text: $index() + 1">11</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13002</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn công nghệ phần mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">24C06</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">12</td>
                <td class="text-center" data-bind="text: KyHieu">PHY00007</td>
                <td class="text-left" data-bind="text: TenMH">Vật lý cho Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">24C07</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">13</td>
                <td class="text-center" data-bind="text: KyHieu">PHY00007</td>
                <td class="text-left" data-bind="text: TenMH">Vật lý cho Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">24C08</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T5 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">14</td>
                <td class="text-center" data-bind="text: KyHieu">PHY00007</td>
                <td class="text-left" data-bind="text: TenMH">Vật lý cho Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">24C09</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">15</td>
                <td class="text-center" data-bind="text: KyHieu">PHY00007</td>
                <td class="text-left" data-bind="text: TenMH">Vật lý cho Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">24C10</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T7 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">16</td>
                <td class="text-center" data-bind="text: KyHieu">PHY00007</td>
                <td class="text-left" data-bind="text: TenMH">Vật lý cho Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">24C11</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">17</td>
                <td class="text-center" data-bind="text: KyHieu">CSC15005</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn mã hóa – mật mã</td>
                <td class="text-center" data-bind="text: MaLopHP">24CNTThuc1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">18</td>
                <td class="text-center" data-bind="text: KyHieu">CSC15006</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn xử lý ngôn ngữ tự nhiên</td>
                <td class="text-center" data-bind="text: MaLopHP">24CNTThuc1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">19</td>
                <td class="text-center" data-bind="text: KyHieu">CSC15005</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn mã hóa – mật mã</td>
                <td class="text-center" data-bind="text: MaLopHP">24CNTThuc2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">20</td>
                <td class="text-center" data-bind="text: KyHieu">CSC15006</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn xử lý ngôn ngữ tự nhiên</td>
                <td class="text-center" data-bind="text: MaLopHP">24CNTThuc2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">21</td>
                <td class="text-center" data-bind="text: KyHieu">CSC15006</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn xử lý ngôn ngữ tự nhiên</td>
                <td class="text-center" data-bind="text: MaLopHP">24CNTThuc3</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">22</td>
                <td class="text-center" data-bind="text: KyHieu">CSC12002</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở dữ liệu nâng cao</td>
                <td class="text-center" data-bind="text: MaLopHP">24HTTT1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">23</td>
                <td class="text-center" data-bind="text: KyHieu">CSC12003</td>
                <td class="text-left" data-bind="text: TenMH">Hệ quản trị cơ sở dữ liệu</td>
                <td class="text-center" data-bind="text: MaLopHP">24HTTT1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">24</td>
                <td class="text-center" data-bind="text: KyHieu">CSC12109</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống thông tin doanh nghiệp</td>
                <td class="text-center" data-bind="text: MaLopHP">24HTTT1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">25</td>
                <td class="text-center" data-bind="text: KyHieu">CSC12002</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở dữ liệu nâng cao</td>
                <td class="text-center" data-bind="text: MaLopHP">24HTTT2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">26</td>
                <td class="text-center" data-bind="text: KyHieu">CSC12003</td>
                <td class="text-left" data-bind="text: TenMH">Hệ quản trị cơ sở dữ liệu</td>
                <td class="text-center" data-bind="text: MaLopHP">24HTTT2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">27</td>
                <td class="text-center" data-bind="text: KyHieu">CSC12109</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống thông tin doanh nghiệp</td>
                <td class="text-center" data-bind="text: MaLopHP">24HTTT2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">28</td>
                <td class="text-center" data-bind="text: KyHieu">CSC12002</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở dữ liệu nâng cao</td>
                <td class="text-center" data-bind="text: MaLopHP">24HTTT3</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">29</td>
                <td class="text-center" data-bind="text: KyHieu">CSC17104</td>
                <td class="text-left" data-bind="text: TenMH">Lập trình cho khoa học dữ liệu</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHDL</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">30</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14119</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn khoa học dữ liệu</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHDL1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">31</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14119</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn khoa học dữ liệu</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHDL2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">32</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14008</td>
                <td class="text-left" data-bind="text: TenMH">Phương pháp nghiên cứu khoa học</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHMT</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">33</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14004</td>
                <td class="text-left" data-bind="text: TenMH">Khai thác dữ liệu và ứng dụng</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHMT1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">34</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14005</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn học máy</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHMT1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">35</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14004</td>
                <td class="text-left" data-bind="text: TenMH">Khai thác dữ liệu và ứng dụng</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHMT2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">36</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14005</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn học máy</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHMT2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">37</td>
                <td class="text-center" data-bind="text: KyHieu">CSC14005</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn học máy</td>
                <td class="text-center" data-bind="text: MaLopHP">24KHMT3</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">38</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13008</td>
                <td class="text-left" data-bind="text: TenMH">Phát triển ứng dụng web</td>
                <td class="text-center" data-bind="text: MaLopHP">24KTPM1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">39</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13102</td>
                <td class="text-left" data-bind="text: TenMH">Lập trình ứng dụng Java</td>
                <td class="text-center" data-bind="text: MaLopHP">24KTPM1</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">40</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13008</td>
                <td class="text-left" data-bind="text: TenMH">Phát triển ứng dụng web</td>
                <td class="text-center" data-bind="text: MaLopHP">24KTPM2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">41</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13102</td>
                <td class="text-left" data-bind="text: TenMH">Lập trình ứng dụng Java</td>
                <td class="text-center" data-bind="text: MaLopHP">24KTPM2</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">42</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13008</td>
                <td class="text-left" data-bind="text: TenMH">Phát triển ứng dụng web</td>
                <td class="text-center" data-bind="text: MaLopHP">24KTPM3</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">43</td>
                <td class="text-center" data-bind="text: KyHieu">CSC13008</td>
                <td class="text-left" data-bind="text: TenMH">Phát triển ứng dụng web</td>
                <td class="text-center" data-bind="text: MaLopHP">24KTPM4</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">44</td>
                <td class="text-center" data-bind="text: KyHieu">CSC11004</td>
                <td class="text-left" data-bind="text: TenMH">Mạng máy tính nâng cao</td>
                <td class="text-center" data-bind="text: MaLopHP">24MMT</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">45</td>
                <td class="text-center" data-bind="text: KyHieu">CSC16001</td>
                <td class="text-left" data-bind="text: TenMH">Đồ họa máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">24TGMT</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">46</td>
                <td class="text-center" data-bind="text: KyHieu">CSC16005</td>
                <td class="text-left" data-bind="text: TenMH">Xử lý ảnh số và video số</td>
                <td class="text-center" data-bind="text: MaLopHP">24TGMT</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">47</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C01</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">48</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C01</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">49</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10008</td>
                <td class="text-left" data-bind="text: TenMH">Mạng máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C01</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">50</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C01</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">51</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C01</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">52</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C02</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">53</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C02</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">54</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10008</td>
                <td class="text-left" data-bind="text: TenMH">Mạng máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C02</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-09:10 <br>T6 07:30-09:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">55</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C02</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">56</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C02</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">57</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C03</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">58</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C03</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">59</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10008</td>
                <td class="text-left" data-bind="text: TenMH">Mạng máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C03</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">60</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C03</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T7 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">61</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C03</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T5 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">62</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C04</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">63</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C04</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">64</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10008</td>
                <td class="text-left" data-bind="text: TenMH">Mạng máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C04</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">65</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C04</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">66</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C04</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">67</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C05</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">68</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C05</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">69</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10008</td>
                <td class="text-left" data-bind="text: TenMH">Mạng máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C05</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">70</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C05</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">71</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C05</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">72</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C06</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">73</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C06</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">74</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10009</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C06</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">75</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C06</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">76</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C06</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">77</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C07</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">60</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/60</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">78</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C07</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">79</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10009</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C07</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">80</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C07</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">81</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C07</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">60</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/60</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">82</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00005</td>
                <td class="text-left" data-bind="text: TenMH">Kinh tế đại cương</td>
                <td class="text-center" data-bind="text: MaLopHP">25C08</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">60</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/60</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">83</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C08</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">84</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10009</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C08</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">85</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C08</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">86</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00006</td>
                <td class="text-left" data-bind="text: TenMH">Vi tích phân 2</td>
                <td class="text-center" data-bind="text: MaLopHP">25C08</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">60</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/60</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">87</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C09</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">88</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10009</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C09</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">89</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C09</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">90</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C10</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">91</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10009</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C10</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">92</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10014</td>
                <td class="text-left" data-bind="text: TenMH">Tư duy tính toán</td>
                <td class="text-center" data-bind="text: MaLopHP">25C10</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">93</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00021</td>
                <td class="text-left" data-bind="text: TenMH">Thể dục 1</td>
                <td class="text-center" data-bind="text: MaLopHP">25C11</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">94</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10009</td>
                <td class="text-left" data-bind="text: TenMH">Hệ thống máy tính</td>
                <td class="text-center" data-bind="text: MaLopHP">25C11</td>
                <td class="text-center" data-bind="text: SoTinChi">2</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">95</td>
                <td class="text-center" data-bind="text: KyHieu">BAA00030</td>
                <td class="text-left" data-bind="text: TenMH">Giáo dục quốc phòng - An ninh</td>
                <td class="text-center" data-bind="text: MaLopHP">25CTT_DKD</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT"></td>
                <td class="text-center" data-bind="html: LichHocTH"></td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">600</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">514/600</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">96</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C01</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">97</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C01</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">98</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C01</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">99</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C01</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">100</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C02</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">101</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C02</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">102</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C02</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T5 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">103</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C02</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">104</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C03</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">105</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C03</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 09:30-11:10 <br>T6 09:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">106</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C03</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T7 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">107</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C03</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">108</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C04</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">109</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C04</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T7 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">110</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C04</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">111</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C04</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">112</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C05</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T7 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T5 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">113</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C05</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">114</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C05</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T7 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">115</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C05</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T5 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">116</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C06</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T7 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">117</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C06</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">118</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C06</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">75</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/75</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">119</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C07</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T7 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">120</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C07</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-09:10 <br>T4 07:30-09:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">121</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C07</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T5 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">122</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C07</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">60</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/60</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">123</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C08</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">124</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C08</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">125</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C08</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">126</td>
                <td class="text-center" data-bind="text: KyHieu">MTH00009</td>
                <td class="text-left" data-bind="text: TenMH">Toán rời rạc</td>
                <td class="text-center" data-bind="text: MaLopHP">26C08</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">60</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/60</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">127</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C09</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">128</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C09</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">129</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C09</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T6 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T4 07:30-09:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">130</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C10</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T5 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">131</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C10</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T2 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">132</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C10</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">133</td>
                <td class="text-center" data-bind="text: KyHieu">CSC00004</td>
                <td class="text-left" data-bind="text: TenMH">Nhập môn Công nghệ thông tin</td>
                <td class="text-center" data-bind="text: MaLopHP">26C11</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T2 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T3 09:30-11:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">134</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10012</td>
                <td class="text-left" data-bind="text: TenMH">Cơ sở lập trình</td>
                <td class="text-center" data-bind="text: MaLopHP">26C11</td>
                <td class="text-center" data-bind="text: SoTinChi">4</td>

                <td class="text-center" data-bind="html: LichHocLT">T3 13:30-17:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 15:30-17:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        
            <tr data-bind="style: { 'background-color': MaLopSH === $root.svDetails().MaLopSH ? 'beige' : '' }">
                <td class="text-center" data-bind="text: $index() + 1">135</td>
                <td class="text-center" data-bind="text: KyHieu">CSC10121</td>
                <td class="text-left" data-bind="text: TenMH">Kỹ năng mềm</td>
                <td class="text-center" data-bind="text: MaLopHP">26C11</td>
                <td class="text-center" data-bind="text: SoTinChi">3</td>

                <td class="text-center" data-bind="html: LichHocLT">T4 07:30-11:10 </td>
                <td class="text-center" data-bind="html: LichHocTH">T6 13:30-15:30</td>

                <td class="text-center" data-bind="visible: $parent.svDetails().LoaiSV == 'CLC'">
                    <i class="fas fa-check-circle text-success" data-bind="visible: HocBangTA" style="display: none;">
                </i></td>

                <td class="text-center" data-bind="text: SoSVDK">50</td>
                <td class="text-center" data-bind="text: SoSVTT, visible: $root.ok" style="display: none;">0/50</td>
                
                
            </tr>
        </tbody>
    </table>
"""
